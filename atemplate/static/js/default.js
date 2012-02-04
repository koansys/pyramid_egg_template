/*global document:true, $:true window:true */
/*jslint indent:4 maxlen:80 */
// Default JS file

/*

To configure the warn if modified alert do something like the following:

            $(':input', "#id").bind("change", function() {
                   window.onbeforeunload = WarnModified;x
                       $("button").click(function(){
                           window.onbeforeunload = DontWarnModified;
                           });
                   }); // Prevent accidental navigation away

         });

*/

function WarnIfError() {
    "use strict";
    return "Any unsaved changes to this form will be lost.\n\n" +
           "Fix any errors on this form by looking for any section " +
           "tab to the left of the form body that has an '!' in a red " +
           "circle.\n\nSelect each tab marked as having errors and scroll " +
           "through it correcting errors in any form field marked as having " +
           "an error.\n\nYou should then click save or submit at the " +
           "bottom of this form to preserve your changes.";
}
function WarnModified() {
    "use strict";
    return "Any unsaved changes to this form will be lost.\n\n" +
           "You should click save or submit at the bottom of " +
           "this form to preserve your changes.";
}
function DontWarnModified()  {
    "use strict"; /* nothing to return */
}
// Popup window code
// <a href="Javascript:aPopup(url)" >link text</a>
function aPopup(url) {
    "use strict";
    var popupWindow = window.open(
	url,
        'popUpWindow',
        'height=700,width=1000,left=10,top=10,resizable=yes,' +
            'scrollbars=yes,toolbar=yes,menubar=no,location=no,' +
            'directories=no,status=yes');
}

$(document).ready(function () {
    "use strict";
    // JQ code here
});