# This module contains pre_process_js which is called by hallgrimJS.py to pre-process all javaScript-relevant parts, including adding imports and
# replacing the tags. It furthermore contains base-functionality which is vital to the operation of the produced javaScript and its use.

import re
import base64
import os
from . import javaScriptTagProcessing
from . import javaScriptMiscTools
from .JSComponents import JSDrawingCanvas, JSEditor, JSGraphEditor, JSVariableTable, JSVirtualMachine
MARKDOWN_CONVERTER_SOURCE = "https://cdn.jsdelivr.net/npm/showdown@1.9.0"
CODE_EDITOR_SOURCE = "https://pagecdn.io/lib/ace/1.4.6/ace.js"
DOM_PURIFIER_SOURCE = "https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.1.1/purify.min.js"

# pushes given message into container on error
# this concerns errors on startup and is only applied where sensible (i.e. in places where website parts are replaced - code which is purely internal should not need this)
def addErrorReporting(code, message):
    return "try{" + code + "} catch(e){HGErrorMessages.push('" + message + " :' + e.message);}"

# for putting some functions outside of the local context in the case of the first instance
# this is done here instead of just writing these functions outside of the function for this instance because some of these are instance dependent and we would prefer to just use the first instance where any version is needed
# this could be split up and put by the original definition if you like, but I chose to collect all these here for a better overview
INSTANCEGLOBALIZER = """
if(HGInstance == 0){
  HGGlobalize(HGToB64, "HGToB64");
  HGGlobalize(HGFromB64, "HGFromB64");
  HGGlobalize(HGSaveAndClick, "HGSaveAndClick");
  HGGlobalize(HGElement, "HGElement");
  HGGlobalize(HGFinishAll, "HGFinishAll");
  HGGlobalize(HGTimeEnder,"HGTimeEnder");
}
"""

def import_string(source):
    return """<script src = {Fsource}></script>""".format(Fsource = source);

# should remove itself if javascript execution successful (at least initially)
ERROR_MESSAGE_WITH_REMOVER = ("""<h1 HGID = 'NOJAVASCRIPTERROR'>FALLS DIESER TEXT NICHT VERSCHWINDET GAB ES EIN PROBLEM MIT DER AUSFÜHRUNG VON JAVASCRIPT. DIES BEEINTRÄCHTIGT MÖGLICHERWEISE DIE FUNKTIONSFÄHIGKEIT DER AUFGABE. STELLEN SIE SICHER, DASS IHR BROWSER NICHT VERALTET IST UND SIE PLUGINS DEAKTIVIEREN, WELCHE JAVASCRIPT AUF ILIAS BLOCKIEREN! KONTAKTIEREN SIE ANDERNFALLS EINEN TUTOR!</h1>""",
"""
if(HGErrorMessages.length == 0){
  for(var copyNum = 0; copyNum < HGElements('NOJAVASCRIPTERROR').length; copyNum++){
    HGElements('NOJAVASCRIPTERROR')[copyNum].style.display = 'none';
  }
}
else{
  message = "Critical errors on task startup:";
  for(var msn = 0; msn < HGErrorMessages.length; msn++){
    message += "\\n" + HGErrorMessages[msn]
  }
  alert(message);
}
"""
)

def pre_process_js(code, task):
    """Adds functions and function calls for automatic processing of inputs and outputs, management of submissions and abstraction for additional provided functionality and DOM-JS-Interaction. Also adds the needed imports."""
    imp = ""; # imports
    imp = import_string(DOM_PURIFIER_SOURCE) + imp;
    basedir = os.path.dirname(os.path.abspath(__file__))
    (task , converters) = javaScriptTagProcessing.hg_js_tag_processor(task) # process tags
    code = addErrorReporting(code, "Error in user code")
    code = converters + code;
    (errorM, errorR) = ERROR_MESSAGE_WITH_REMOVER
    task = errorM + task # add error message to task
    code = code + errorR # remove warning after all other code has run
    #following parts add imports if relevant function calls are detected
    if("HGMDAndAMToHTML(" in code):
        imp = import_string(MARKDOWN_CONVERTER_SOURCE) + imp
        with open(os.path.join(basedir,"ASCIIMathTeXImg.js"),"r") as conv_file:
            code = conv_file.read() + code
        code = javaScriptMiscTools.MD_AND_AM_TO_HTML + code 
    reg = re.compile('HGProcessLatex\(', re.MULTILINE)
    code = re.sub(reg, "MathJax.Hub.Typeset(", code)
    if("HGRunPython(" in code):
        code = javaScriptMiscTools.SKULPT_PY + code
        with open(os.path.join(basedir,"skulpt-stdlib.js"),"r") as conv_file:
            code = conv_file.read() + code
        with open(os.path.join(basedir,"skulpt.min.js"),"r") as conv_file:
            code = conv_file.read() + code
    if("HGEditor(" in code):
        imp = import_string(CODE_EDITOR_SOURCE) + imp;
        code = JSEditor.CODE_EDITOR + code
    if("HGVariableTable(" in code):
        code = JSVariableTable.VARIABLE_TABLE + code
    if("HGDrawingCanvas(" in code):
        imp = import_string(CODE_EDITOR_SOURCE) + imp;
        code = JSDrawingCanvas.DRAWING_CANVAS + code
    if("HGGraphEditor(" in code):
        code = JSGraphEditor.GRAPH_EDITOR + code
        with open(os.path.join(basedir,"vis-network.min.js"),"r") as conv_file:
            code = conv_file.read() + code
    if("HGMakeVM(" in code or "HGMakeStateVM(" in code):
        code = JSVirtualMachine.VIRTUAL_MACHINE + code
        with open(os.path.join(basedir,"v86_ext.js"),"r") as emu_file:
            code = emu_file.read() + code
    return (code, imp, task)
