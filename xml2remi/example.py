from remi import server, gui

class MyApp(server.App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
    
    def main(self):
        root = gui.VBox()
        root_Label_0 = gui.Label(text="Hello World")
        root.append(root_Label_0)

        root_Button_1 = gui.Button(text="Click Me")
        root.append(root_Button_1)

        root_TabBox_2 = gui.TabBox()
        root_TabBox_2_VBox_0 = gui.VBox()
        root_TabBox_2_VBox_0_Label_0 = gui.Label(text="Content of Tab 1")
        root_TabBox_2_VBox_0.append(root_TabBox_2_VBox_0_Label_0)
        root_TabBox_2.append(root_TabBox_2_VBox_0)

        root_TabBox_2_HBox_1 = gui.HBox()
        root_TabBox_2_HBox_1_TextInput_0 = gui.TextInput()
        root_TabBox_2_HBox_1.append(root_TabBox_2_HBox_1_TextInput_0)

        root_TabBox_2_HBox_1_CheckBox_1 = gui.CheckBox()
        root_TabBox_2_HBox_1.append(root_TabBox_2_HBox_1_CheckBox_1)
        root_TabBox_2.append(root_TabBox_2_HBox_1)
        root.append(root_TabBox_2)

        # add your code here
        
        return root

if __name__ == "__main__":
    server.start(MyApp)
