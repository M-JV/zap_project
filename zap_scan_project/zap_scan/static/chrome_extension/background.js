console.log("Background script loaded");

chrome.browserAction.onClicked.addListener(function(tab) {
    console.log("Browser action clicked");
    submitUrlAsForm(tab);
});

function submitUrlAsForm(tab) {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var url = tabs[0].url;
        chrome.runtime.sendMessage({url: url});
    });
}
