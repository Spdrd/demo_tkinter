from customtkinter import *

class t_display:

    def __init__(self, elements, elements_types):
        self.elements = elements
        self.elements_types = elements_types
        self.combo_index = 0
        for i in range(len(elements)):
            elements[i][0].grid(row=i, column=0, padx=10, pady=10)
            elements[i][1].grid(row=i, column=1, padx=10, pady=10)
            elements[i][2].grid(row=i, column=2, padx=10, pady=10)

    def get_info(self):
        self.combo_index = 0
        info = []
        for i in range(len(self.elements)):
            info_element =self.check_type(self.elements[i][1].get(), 
                                          self.elements_types[i], 
                                          self.elements[i][2])
            if info_element == -1:
                return -1
            info.append(info_element)
        return info
    
    def check_type(self, info, type, mesage_label):
        if type == "num":
            try:
                info = int(info)
            except:
                mesage_label.configure(text="Este valor debe ser numerico")
                return -1
        if type == "combo":
            print(f"t_display: {info}")

        return info

    

    def get_pk(self):
        return self.check_type(self.elements[0][1].get(), self.elements_types[0], self.elements[0][2])
    
    def set_info(self, info):
        for i in range(len(info)-1):
            self.elements[i][1].delete(0, END)
            self.elements[i][1].insert(0, info[i])