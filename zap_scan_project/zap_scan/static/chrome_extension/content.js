console.log("Content script injected");

window.addEventListener('hashchange', function() {
    var url = window.location.href;
    chrome.runtime.sendMessage({url: url});
});

window.addEventListener('popstate', function() {
    var url = window.location.href;
    chrome.runtime.sendMessage({url: url});
});

window.addEventListener('load', function() {
    var url = window.location.href;
    chrome.runtime.sendMessage({url: url});
});
