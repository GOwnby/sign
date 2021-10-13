var requestID = document.getElementById("requestID").innerHTML;
var fileLocation = '/../../media/documents/' + requestID + ".pdf"; 

var loadingTask = pdfjsLib.getDocument(fileLocation);


var currPage = 1; //Pages are 1-based not 0-based
var numPages = 0;
var thePDF = null;

//This is where you start
loadingTask.promise.then(function(pdf) {

        //Set PDFJS global object (so we can easily access in our page functions
        thePDF = pdf;

        //How many pages it has
        numPages = pdf.numPages;

        //Start with first page
        pdf.getPage( 1 ).then( handlePages );
});



function handlePages(page)
{
    //This gives us the page's dimensions at full scale
    var viewport = page.getViewport( 1 );

    //We'll create a canvas for each page to draw it on
    var canvas = document.createElement("page");
    canvas.style.display = "block";
    var context = canvas.getContext("2d");
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    //Draw it on the canvas
    page.render({canvasContext: context, viewport: viewport});

    //Add it to the web page
    document.getElementById("canvas").appendChild(canvas);

    //Move to next page
    currPage++;
    if ( thePDF !== null && currPage <= numPages )
    {
        thePDF.getPage( currPage ).then( handlePages );
    }
}

// this

document.getElementById("Sign").onclick(function() {

    var thisBox = document.createElement("div");
    thisBox.className = "box";

    var frame = document.getElementById("frame");

    frame.onclick(function(event) {
        var x = event.clientX;
        var y = event.clientY;
        
    });

});

var docDiv = document.getElementById("docDiv");

var iframe = document.createElement("iframe");
var fileString = "/media/documents/" + document.getElementById("requestID").innerText + ".pdf"
iframe.setAttribute("id", "iframe");
iframe.setAttribute("class", "iframe")
iframe.setAttribute("src", fileString);
iframe.setAttribute("width", "100%");
iframe.setAttribute("height", "100%");
iframe.setAttribute("scrolling", "auto");

docDiv.appendChild(iframe);
