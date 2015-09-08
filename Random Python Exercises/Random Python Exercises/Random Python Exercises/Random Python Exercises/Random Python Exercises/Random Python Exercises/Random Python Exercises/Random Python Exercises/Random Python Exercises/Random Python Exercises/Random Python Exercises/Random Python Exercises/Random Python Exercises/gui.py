import simplegui
g = simplegui.GUI()
def buttoncallback():
    g.status("Button klicked!")
g.button("Klick me!", buttoncallback)
g.button("Klick me too!", buttoncallback)
def listboxcallback(text):
    g.status("listbox select: '{0}'".format(text))
g.listbox(["one", "two", "three"], listboxcallback)
g.listbox(["A", "B", "C"], listboxcallback)
def scalecallback(text):
    g.status("scale value: '{0}'".format(text))
g.scale("Scale me!", scalecallback)
g.run()

