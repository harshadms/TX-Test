#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TX Test
# Author: harshadms
# Generated: Thu Apr  4 09:51:56 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import histosink_gl
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class tx_test(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="TX Test")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sampno = sampno = 32
        self.samp_rate_1 = samp_rate_1 = sampno*1e3
        self.sigsource = sigsource = 100
        self.samp_rate = samp_rate = int(samp_rate_1)
        self.carfreqno = carfreqno = 1
        self.carfreq_1 = carfreq_1 = 1
        self.bbfreqno = bbfreqno = 1
        self.bbfreq_1 = bbfreq_1 = 1
        self.bb_amp = bb_amp = 0

        ##################################################
        # Blocks
        ##################################################
        self._bbfreqno_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.bbfreqno,
        	callback=self.set_bbfreqno,
        	label='Baseband Frequency',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._bbfreqno_text_box, 0, 0, 1, 1)
        self._sigsource_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.sigsource,
        	callback=self.set_sigsource,
        	label='Signal Source',
        	choices=[100,101,102,103,104,105],
        	labels=['Constant', 'Sine Wave', 'Cosine Wave', 'Square', 'Triange', 'Saw Tooth'],
        )
        self.GridAdd(self._sigsource_chooser, 7, 0, 1, 1)
        self._sampno_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.sampno,
        	callback=self.set_sampno,
        	label='Sample Rate',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._sampno_text_box, 4, 0, 1, 1)
        self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Scope Sink")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "FFT Sink")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Histo Sink")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Waterfall Sink")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Constellation Sink")
        self.GridAdd(self.notebook, 8, 0, 1, 1)
        self._carfreqno_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.carfreqno,
        	callback=self.set_carfreqno,
        	label='Carrier Frequency',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._carfreqno_text_box, 2, 0, 1, 1)
        self._bbfreq_1_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.bbfreq_1,
        	callback=self.set_bbfreq_1,
        	label=' ',
        	choices=[bbfreqno,bbfreqno*1e3,bbfreqno*1e6,bbfreqno*1e9],
        	labels=['Hz','kHz','MHz','GHz'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._bbfreq_1_chooser, 1, 0, 1, 1)
        _bb_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_amp_sizer,
        	value=self.bb_amp,
        	callback=self.set_bb_amp,
        	label='Baseband Amplitude',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_amp_sizer,
        	value=self.bb_amp,
        	callback=self.set_bb_amp,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_bb_amp_sizer, 6, 0, 1, 1)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.notebook.GetPage(3).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        	win=window.hanning,
        )
        self.notebook.GetPage(3).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(0).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_histosink2_0 = histosink_gl.histo_sink_f(
        	self.notebook.GetPage(2).GetWin(),
        	title='Histogram Plot',
        	num_bins=27,
        	frame_size=1000,
        )
        self.notebook.GetPage(2).Add(self.wxgui_histosink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.notebook.GetPage(4).GetWin(),
        	title='Constellation Plot',
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.notebook.GetPage(4).Add(self.wxgui_constellationsink2_0.win)
        self._samp_rate_1_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.samp_rate_1,
        	callback=self.set_samp_rate_1,
        	label=' ',
        	choices=[sampno,sampno*1e3,sampno*1e6,sampno*1e9],
        	labels=['sp/s','ksp/s','msp/s','gsp/s'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._samp_rate_1_chooser, 5, 0, 1, 1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(samp_rate/32000),
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self._carfreq_1_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.carfreq_1,
        	callback=self.set_carfreq_1,
        	label=' ',
        	choices=[carfreqno,carfreqno*1e3,carfreqno*1e6,carfreqno*1e9],
        	labels=['Hz','kHz','MHz','GHz'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._carfreq_1_chooser, 3, 0, 1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(32e3, sigsource, bbfreq_1, bb_amp, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_histosink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_waterfallsink2_0, 0))

    def get_sampno(self):
        return self.sampno

    def set_sampno(self, sampno):
        self.sampno = sampno
        self._sampno_text_box.set_value(self.sampno)
        self.set_samp_rate_1(self.sampno*1e3)

    def get_samp_rate_1(self):
        return self.samp_rate_1

    def set_samp_rate_1(self, samp_rate_1):
        self.samp_rate_1 = samp_rate_1
        self.set_samp_rate(int(self.samp_rate_1))
        self._samp_rate_1_chooser.set_value(self.samp_rate_1)

    def get_sigsource(self):
        return self.sigsource

    def set_sigsource(self, sigsource):
        self.sigsource = sigsource
        self._sigsource_chooser.set_value(self.sigsource)
        self.analog_sig_source_x_0.set_waveform(self.sigsource)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)

    def get_carfreqno(self):
        return self.carfreqno

    def set_carfreqno(self, carfreqno):
        self.carfreqno = carfreqno
        self._carfreqno_text_box.set_value(self.carfreqno)

    def get_carfreq_1(self):
        return self.carfreq_1

    def set_carfreq_1(self, carfreq_1):
        self.carfreq_1 = carfreq_1
        self._carfreq_1_chooser.set_value(self.carfreq_1)

    def get_bbfreqno(self):
        return self.bbfreqno

    def set_bbfreqno(self, bbfreqno):
        self.bbfreqno = bbfreqno
        self._bbfreqno_text_box.set_value(self.bbfreqno)

    def get_bbfreq_1(self):
        return self.bbfreq_1

    def set_bbfreq_1(self, bbfreq_1):
        self.bbfreq_1 = bbfreq_1
        self._bbfreq_1_chooser.set_value(self.bbfreq_1)
        self.analog_sig_source_x_0.set_frequency(self.bbfreq_1)

    def get_bb_amp(self):
        return self.bb_amp

    def set_bb_amp(self, bb_amp):
        self.bb_amp = bb_amp
        self._bb_amp_slider.set_value(self.bb_amp)
        self._bb_amp_text_box.set_value(self.bb_amp)
        self.analog_sig_source_x_0.set_amplitude(self.bb_amp)


def main(top_block_cls=tx_test, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
