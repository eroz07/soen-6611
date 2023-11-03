import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # create input text
        self.text = wx.StaticText(panel, label="Input：")
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)  # multiple line

        # function buttons
        self.minimum_button = wx.Button(panel, label="Minimum")
        self.maximum_button = wx.Button(panel, label="Maximum")
        self.mode_button = wx.Button(panel, label="Mode")
        self.median_button = wx.Button(panel, label="Median")
        self.mean_button = wx.Button(panel, label="Arithmetic Mean")
        self.mad_button = wx.Button(panel, label="MAD")
        self.std_dev_button = wx.Button(panel, label="Standard Deviation")

        # output
        self.result_label = wx.StaticText(panel, label="Output：")
        self.result_text = wx.TextCtrl(panel, style=wx.TE_READONLY)

        # horizontal sizer to organize buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.minimum_button, 0, wx.ALL, 5)
        button_sizer.Add(self.maximum_button, 0, wx.ALL, 5)
        button_sizer.Add(self.mode_button, 0, wx.ALL, 5)
        button_sizer.Add(self.median_button, 0, wx.ALL, 5)
        button_sizer.Add(self.mean_button, 0, wx.ALL, 5)
        button_sizer.Add(self.mad_button, 0, wx.ALL, 5)
        button_sizer.Add(self.std_dev_button, 0, wx.ALL, 5)

        # vertival sizer to organize buttons
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.text, 0, wx.ALL, 5)
        main_sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.result_label, 0, wx.ALL, 5)
        main_sizer.Add(self.result_text, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(main_sizer)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, title="METRICSTICS", size=(750, 400))  # inital window size
    frame.Show()
    app.MainLoop()