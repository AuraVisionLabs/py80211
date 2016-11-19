##
# Module providing scan functionality

#
# Copyright 2015 Arend van Spriel <aspriel@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
import sys
import traceback

import netlink.capi as nl
import netlink.core as nlc
import netlink.genl.capi as genl
import generated.defs as nl80211

from generated.policy import nl80211_policy
from base import *
import factory

bss_policy = nl.nla_policy_array(nl80211.BSS_MAX + 1)
bss_policy[nl80211.BSS_TSF].type = nl.NLA_U64
bss_policy[nl80211.BSS_FREQUENCY].type = nl.NLA_U32
bss_policy[nl80211.BSS_BSSID].type = nl.NLA_UNSPEC
bss_policy[nl80211.BSS_BEACON_INTERVAL].type = nl.NLA_U16
bss_policy[nl80211.BSS_CAPABILITY].type = nl.NLA_U16
bss_policy[nl80211.BSS_INFORMATION_ELEMENTS].type = nl.NLA_UNSPEC
bss_policy[nl80211.BSS_SIGNAL_MBM].type = nl.NLA_U32
bss_policy[nl80211.BSS_SIGNAL_MBM].signed = True
bss_policy[nl80211.BSS_SIGNAL_UNSPEC].type = nl.NLA_U8
bss_policy[nl80211.BSS_STATUS].type = nl.NLA_U32
bss_policy[nl80211.BSS_SEEN_MS_AGO].type = nl.NLA_U32
bss_policy[nl80211.BSS_BEACON_IES].type = nl.NLA_UNSPEC
bss_policy[nl80211.BSS_BEACON_TSF].type = nl.NLA_U64
bss_policy[nl80211.BSS_CHAN_WIDTH].type = nl.NLA_U32
bss_policy[nl80211.BSS_PRESP_DATA].type = nl.NLA_FLAG

class bss(nl80211_object):
	pass

class bss_list(custom_handler):
	def __init__(self, ifidx, kind=nl.NL_CB_DEFAULT):
		self._access = access80211(kind)
		self._ifidx = ifidx
		self.refresh()

	def __iter__(self):
		return iter(self._bss)

	def find_status_bss(self):
		self.refresh()
		for bss in self._bss:
			if nl80211.BSS_STATUS in bss.attrs:
				return bss
		return None

	def refresh(self):
		self._bss = []
		flags = nlc.NLM_F_REQUEST | nlc.NLM_F_ACK | nlc.NLM_F_DUMP
		m = self._access.alloc_genlmsg(nl80211.CMD_GET_SCAN, flags)
		nl.nla_put_u32(m._msg, nl80211.ATTR_IFINDEX, self._ifidx)
		self._access.send(m, self)

	def handle(self, msg, arg):
		try:
			e, attrs = genl.py_genlmsg_parse(nl.nlmsg_hdr(msg), 0, nl80211.ATTR_MAX, None)
			if not nl80211.ATTR_BSS in attrs:
				return
			e, nattrs = nl.py_nla_parse_nested(len(bss_policy), attrs[nl80211.ATTR_BSS], bss_policy)
			self._bss.append(factory.get_inst().create(bss, nattrs, bss_policy))
		except Exception as e:
			(t,v,tb) = sys.exc_info()
			print v.message
			traceback.print_tb(tb)
		return nl.NL_SKIP

class scan_cmd_base(nl80211_cmd_base):
	def __init__(self, ifidx, level=nl.NL_CB_DEFAULT):
		super(scan_cmd_base, self).__init__(ifidx, level)

	def _wait_for_completion(self):
		while self.scan_busy:
			self._access._sock.recvmsgs(self._access._rx_cb)

	def _send_and_wait(self):
		self.scan_busy = True
		self._access.disable_seq_check()
		mcid = self._access.subscribe_multicast('scan')
		ret = self._access.send(self._nl_msg, self)
		if ret < 0:
			self.scan_busy = False
			return ret

		self._wait_for_completion()
		self._access.drop_multicast(mcid)
		return 0

	def send(self):
		self._prepare_cmd()
		self._add_attrs()
		return self._send_and_wait()

class scan_start_base(scan_cmd_base):
	def __init__(self, ifidx, level=nl.NL_CB_DEFAULT):
		super(scan_start_base, self).__init__(ifidx, level)
		self._ssids = None
		self._freqs = None
		self._flags = 0
		self._ies = None

	def _add_attrs(self):
		super(scan_start_base, self)._add_attrs()
		if self._ssids:
			i = 0
			nest = nl.nla_nest_start(self._nl_msg._msg, nl80211.ATTR_SCAN_SSIDS)
			for ssid in self._ssids:
				nl.nla_put(self._nl_msg._msg, i, ssid)
				i += 1
			nl.nla_nest_end(self._nl_msg._msg, nest)
		if self._freqs:
			i = 0
			nest = nl.nla_nest_start(self._nl_msg._msg, nl80211.ATTR_SCAN_FREQUENCIES)
			for freq in self._freqs:
				nl.nla_put_u32(self._nl_msg._msg, i, freq)
				i += 1
			nl.nla_nest_end(self._nl_msg._msg, nest)
		if self._flags != 0:
			nl.nla_put_u32(self._nl_msg._msg, nl80211.ATTR_SCAN_FLAGS, self._flags)
		if self._ies:
			nl.nla_put(self._nl_msg._msg, nl80211.ATTR_IE, self._ies)

	def add_ssids(self, ssids):
		if self._ssids == None:
			self._ssids = ssids
		elif ssids == None:
			self._ssids = None
		else:
			self._ssids = self._ssids + ssids

	def add_freqs(self, freqs):
		if self._freqs == None:
			self._freqs = freqs
		elif freqs == None:
			self._freqs = None
		else:
			self._freqs = self._freqs + freqs

	def set_ies(self, ies):
		self._ies = ies

	def set_flags(self, flags):
		self._flags = flags

class scan_request(scan_start_base):
	def __init__(self, ifidx, level=nl.NL_CB_DEFAULT):
		super(scan_request, self).__init__(ifidx, level)
		self._cmd = nl80211.CMD_TRIGGER_SCAN

	def handle(self, msg, arg):
		genlh = genl.genlmsg_hdr(nl.nlmsg_hdr(msg))

		# A regular scan is complete when we get scan results
		if genlh.cmd in [ nl80211.CMD_SCAN_ABORTED, nl80211.CMD_NEW_SCAN_RESULTS ]:
			self.scan_busy = False
		return nl.NL_SKIP

class sched_scan_start(scan_start_base):
	def __init__(self, ifidx, level=nl.NL_CB_DEFAULT):
		super(sched_scan_start, self).__init__(ifidx, level)
		self._cmd = nl80211.CMD_START_SCHED_SCAN
		self._interval = None
		self._matches = None

	def set_interval(self, interval):
		self._interval = interval

	def add_matches(self, matches):
		self._matches = matches

	def _add_matches_attrs(self):
		if self._matches:
			i = 0

			matchset = nl.nla_nest_start(self._nl_msg._msg, nl80211.ATTR_SCHED_SCAN_MATCH)
			for match in self._matches:
				nest = nl.nla_nest_start(self._nl_msg._msg, i)
				if 'ssid' in match:
					nl.nla_put(self._nl_msg._msg, nl80211.SCHED_SCAN_MATCH_ATTR_SSID, match['ssid'])
				i += 1
				nl.nla_nest_end(self._nl_msg._msg, nest)

			nl.nla_nest_end(self._nl_msg._msg, matchset)

	def _add_attrs(self):
		super(sched_scan_start, self)._add_attrs()
		self._add_matches_attrs()
		if self._interval != None:
			nl.nla_put_u32(self._nl_msg._msg, nl80211.ATTR_SCHED_SCAN_INTERVAL, self._interval)

	def handle(self, msg, arg):
		genlh = genl.genlmsg_hdr(nl.nlmsg_hdr(msg))

		# A schedule scan is complete immediately when it gets started
		if genlh.cmd in [ nl80211.CMD_START_SCHED_SCAN ]:
			self.scan_busy = False
			return nl.NL_SKIP

class sched_scan_stop(scan_cmd_base):
	def __init__(self, ifidx, level=nl.NL_CB_DEFAULT):
		super(sched_scan_stop, self).__init__(ifidx, level)
		self._cmd = nl80211.CMD_STOP_SCHED_SCAN

	def handle(self, msg, arg):
		genlh = genl.genlmsg_hdr(nl.nlmsg_hdr(msg))
		if genlh.cmd in [ nl80211.CMD_SCHED_SCAN_STOPPED ]:
			self.scan_busy = False
		return nl.NL_SKIP
