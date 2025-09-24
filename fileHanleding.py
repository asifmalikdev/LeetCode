# f = open("file.txt", mode="w")
# f.write("hello asif5\n")
# f.write("hello asif this is me\n")
# f.write("hello asif\n")
# f.write("hello asif this is me\n")
# f.close()

# with open("file.txt", mode = "r") as f:
#     content = f.read()
    # print(content)

from graphviz import Digraph

# Create a Digraph
dot = Digraph(comment="Django Views Hierarchy", format="png")
dot.attr(rankdir="TB", fontsize="10")

# Root
dot.node("Views", shape="box", style="filled", color="lightblue")

# Function-Based Views
dot.node("FBV", "Function-Based Views", shape="box", style="rounded,filled", color="lightgreen")
dot.edge("Views", "FBV")
dot.node("CustomFunc", "Custom Functions\ndef my_view(request)", shape="ellipse")
dot.node("Decorators", "Decorators\n@login_required, etc.", shape="ellipse")
dot.edge("FBV", "CustomFunc")
dot.edge("FBV", "Decorators")

# Class-Based Views
dot.node("CBV", "Class-Based Views", shape="box", style="rounded,filled", color="lightyellow")
dot.edge("Views", "CBV")

# Base Views
dot.node("BaseViews", "Base Views", shape="box")
dot.edge("CBV", "BaseViews")
dot.node("View", "View", shape="ellipse")
dot.node("TemplateView", "TemplateView", shape="ellipse")
dot.edge("BaseViews", "View")
dot.edge("BaseViews", "TemplateView")

# Generic Display Views
dot.node("DisplayViews", "Generic Display Views", shape="box")
dot.edge("CBV", "DisplayViews")
dot.node("DetailView", "DetailView", shape="ellipse")
dot.node("ListView", "ListView", shape="ellipse")
dot.edge("DisplayViews", "DetailView")
dot.edge("DisplayViews", "ListView")

# Generic Editing Views
dot.node("EditingViews", "Generic Editing Views", shape="box")
dot.edge("CBV", "EditingViews")
dot.node("CreateView", "CreateView", shape="ellipse")
dot.node("UpdateView", "UpdateView", shape="ellipse")
dot.node("DeleteView", "DeleteView", shape="ellipse")
dot.edge("EditingViews", "CreateView")
dot.edge("EditingViews", "UpdateView")
dot.edge("EditingViews", "DeleteView")

# Form Handling Views
dot.node("FormViews", "Form Handling Views", shape="box")
dot.edge("CBV", "FormViews")
dot.node("FormView", "FormView", shape="ellipse")
dot.node("ProcessFormView", "ProcessFormView", shape="ellipse")
dot.edge("FormViews", "FormView")
dot.edge("FormViews", "ProcessFormView")

# Other CBVs
dot.node("OtherCBV", "Other Useful CBVs", shape="box")
dot.edge("CBV", "OtherCBV")
dot.node("RedirectView", "RedirectView", shape="ellipse")
dot.node("ArchiveViews", "Archive Views\nYear/Month/DayArchiveView", shape="ellipse")
dot.node("DateDetailView", "DateDetailView", shape="ellipse")
dot.edge("OtherCBV", "RedirectView")
dot.edge("OtherCBV", "ArchiveViews")
dot.edge("OtherCBV", "DateDetailView")

# Render output file
output_path = "/mnt/data/django_views_tree"
dot.render(output_path, cleanup=True)

output_path + ".png"
