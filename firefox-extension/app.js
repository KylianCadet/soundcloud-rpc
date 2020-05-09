const url = "ws://localhost:8765"
var webSocket = new WebSocket(url);

document.onchange = function (event) {
  console.log("document has changed")
}

var panel = document.querySelector(".playControls__soundBadge")
var title = document.querySelector(".playbackSoundBadge__avatar")
var progress = document.querySelector(".playbackTimeline__progressWrapper")
var play = document.querySelector(".playControls__play")
var last_title = title.getAttribute("href")
var counter = 1;

progress.addEventListener("DOMAttrModified", () => {
  if (counter--)
    return
  counter = 1
  var msg = {
    "type": "progress",
    "valuetext": progress.getAttribute("aria-valuetext"),
    "valueint": parseInt(progress.getAttribute("aria-valuenow"), 10)
  }
  // progress update
  sendMessage(msg)
})

panel.addEventListener("DOMAttrModified", () => {
  title = document.querySelector(".playbackSoundBadge__avatar")
  if (title.getAttribute("href") == last_title) {
    // Same title, play button has been triggered
    updatePlay()
  } else {
    // Not the same title, big update
    update()
    last_title = title.getAttribute("href")
  }
})

function sendMessage(msg) {
  console.log(msg)
  webSocket.send(JSON.stringify(msg))
}

function updatePlay() {
  var msg = {
    "type": "play",
    "value": play.classList.contains("playing")
  }
  sendMessage(msg)
}

function update() {
  var msg = {
    "type": "update",
    "url": "https://soundcloud.com" + title.getAttribute("href"),
    "valuetext": progress.getAttribute("aria-valuetext"),
    "valueint": parseInt(progress.getAttribute("aria-valuenow"), 10),
    "playing": play.classList.contains("playing")
  }
  sendMessage(msg)
}

webSocket.onopen = function (event) {
  update();
};

webSocket.onmessage = function (event) {
  update();
}