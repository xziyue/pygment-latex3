import wx
from pygments import highlight
from tex_lexer import Tex3Lexer
from pygments.formatters.html import HtmlFormatter


class MyFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self)

        self.SetSize(wx.Size(800, 600))
        self.SetTitle('Highlight LaTeX3')

        self.textIn = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.textOut = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(self.textIn, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.textOut, 1, wx.ALL | wx.EXPAND, 10)

        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnConv = wx.Button(self.panel, label='Convert')
        self.btnConv.Bind(wx.EVT_BUTTON, self.evtBtn)
        hSizer.Add(self.btnConv, 1, wx.ALL | wx.ALIGN_CENTER, 10)

        sizer.Add(hSizer, 0, wx.ALL | wx.EXPAND)

        self.panel.SetSizerAndFit(sizer)

        self.Show()

    def evtBtn(self, evt):
        inText = self.textIn.GetValue()
        output = highlight(inText, Tex3Lexer(), HtmlFormatter())
        self.textOut.SetValue(output)


app = wx.App()
MyFrame(None)
app.MainLoop()