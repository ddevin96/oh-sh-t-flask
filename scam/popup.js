
 window.addEventListener("DOMContentLoaded", function() {

    /*this.document.querySelector("#onoff").addEventListener("click", function() {
        if(document.querySelector("#onoff").innerHTML == "Start") {
            document.querySelector("#onoff").innerHTML="Stop";
        } else {
            document.querySelector("#onoff").innerHTML="Start";
        }
    });*/
     this.document.querySelector("#onoff").addEventListener("click", function() {
            //debugger;
            getDataFromChromeTab().then((highlithedText) => {
                // const url = "https://localhost:5000/test";
                const url = "http://127.0.0.1:5000/predictline";
                const options = {
                    method: "POST",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json;charset=UTF-8",
                    },
                    body: JSON.stringify({
                        // textToAnalyze: btoa(highlithedText),
                        textToAnalyze: highlithedText,
                    }),
                    };
                    fetch(url, options)
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);
                    });
            });
    });

    this.document.querySelector("#page").addEventListener("click", function() {
        //debugger;
        getDocumentPage().then((texts) => {
            // const url = "https://localhost:5000/test";
            const url = "http://127.0.0.1:5000/predictpage";
            const options = {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json;charset=UTF-8",
                },
                body: JSON.stringify({
                    // textToAnalyze: btoa(highlithedText),
                    textToAnalyze: texts,
                }),
                };
                fetch(url, options)
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                });
        });
});
    
});

async function getDataFromChromeTab() {

    const [tab] =  await chrome.tabs.query({active: true, currentWindow: true});
    let result;
    try {
      [{result}] = await chrome.scripting.executeScript({
        target: {tabId: tab.id},
        function: () => getSelection().toString(),
      });
    } catch (e) {
      return; // ignoring an unsupported page like chrome://extensions
    }
    return result;
}

async function getDocumentPage() {
    console.log("getDocumentPage");
    const [tab] =  await chrome.tabs.query({active: true, currentWindow: true});
    let result;
    try {
        [{result}] = await chrome.scripting.executeScript({
            target: {tabId: tab.id},
            function: () => {
            return Array.from(
              document.getElementsByTagName('p'),
              el => el.innerHTML
            );},
          });
      } catch (e) {
        return; // ignoring an unsupported page like chrome://extensions
      }
      return result;
}

