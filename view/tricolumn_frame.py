import customtkinter


class TripleColumnFrame(customtkinter.CTkFrame):
    def __init__(self,
                 master,
                 width=940,
                 height=50,
                 column_1_element=None,
                 column_2_element=None,
                 column_3_element=None,
                 **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)

        column_1_width = int((20/100)*(width-20))  # column 1 width equals 20% of total width
        column_2_width = int((60/100)*(width-20))  # column 2 width equals 60% of total width
        column_3_width = width - 20 - column_1_width - column_2_width  # column 3 width equals remaining 20% width

        self.column_1 = customtkinter.CTkFrame(self, width=column_1_width, **kwargs)
        self.column_1.grid(row=0, column=0)
        self.column_1.grid_columnconfigure(index=0, weight=1)
        self.column_1.grid_propagate(False)

        if column_1_element:
            self.column_1_element = column_1_element[0](master=self.column_1, **column_1_element[1])
            self.column_1_element.grid(row=0, column=0)
        else:
            self.column_1_element = None

        self.column_2 = customtkinter.CTkFrame(self, width=column_2_width, **kwargs)
        self.column_2.grid(row=0, column=1)
        self.column_2.grid_columnconfigure(index=0, weight=1)
        self.column_2.grid_propagate(False)

        if column_2_element:
            self.column_2_element = column_2_element[0](master=self.column_2, **column_2_element[1])
            self.column_2_element.grid(row=0, column=0)
        else:
            self.column_2_element = None

        self.column_3 = customtkinter.CTkFrame(self, width=column_3_width, **kwargs)
        self.column_3.grid(row=0, column=2)
        self.column_3.grid_propagate(False)

        if column_3_element:
            self.column_3_element = column_3_element[0](master=self.column_3, **column_3_element[1])
            self.column_3_element.grid(row=0, column=0)
        else:
            self.column_3_element = None
