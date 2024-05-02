// popup.js

$(document).ready(function () {
    // Function to update progress bars and risk level
    function updateProgressBars(data) {
      const highCount = data.high_count;
      const mediumCount = data.medium_count;
      const lowCount = data.low_count;
      const totalCount = data.total_count;
      const riskLevel = data.risk_level;
  
      // Update progress bars
      $(".progress-bar.bg-danger").css("width", `${(highCount / totalCount) * 100}%`).text(highCount);
      $(".progress-bar.bg-warning").css("width", `${(mediumCount / totalCount) * 100}%`).text(mediumCount);
      $(".progress-bar.bg-success").css("width", `${(lowCount / totalCount) * 100}%`).text(lowCount);
      $(".progress-bar.bg-info").css("width", "100%").text(totalCount);
  
      // Update risk level
      $("#riskLevel").text(riskLevel);
    }
  
    // Function to fetch scan results from backend
    function fetchScanResults() {
      $.ajax({
        url: "http://localhost:8000/scan/",
        method: "GET",
        success: function (data) {
          updateProgressBars(data);
        },
        error: function (error) {
          console.error("Error fetching scan results:", error);
        }
      });
    }
  
    // Fetch scan results on popup load
    fetchScanResults();
  
    // Fetch scan results every time popup is opened
    chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
      if (changeInfo.status === "complete") {
        fetchScanResults();
      }
    });
  });
  