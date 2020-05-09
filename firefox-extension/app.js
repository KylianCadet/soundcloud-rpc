const url = "ws://localhost:8765"
var webSocket = new WebSocket(url);

var image = null
var panel = null
var title = null
var user = null
var progress = null
var play = null
var last_title = null
var counter = 1;

function updateData() {
  image = document.querySelector("a.playbackSoundBadge__avatar > div")
  image = image.firstElementChild.getAttribute("style")
  image = image.substr(image.indexOf("\"") + 1, image.length)
  image = image.substr(0, image.indexOf("\""))
  image = image.replace("50x50", "500x500")

  panel = document.querySelector(".playControls__soundBadge")
  user = document.querySelector(".playbackSoundBadge__titleContextContainer > a")
  user = user.getAttribute("title")

  title = document.querySelector(".playbackSoundBadge__titleContextContainer > div > a")
  title = title.getAttribute("title")
  last_title = title

  progress = document.querySelector(".playbackTimeline__progressWrapper")
  play = document.querySelector(".playControls__play")
}

function progressModified() {
  if (counter--)
    return
  counter = 1
  const msg = {
    "type": "progress",
    "valuetext": progress.getAttribute("aria-valuetext"),
    "valueint": parseInt(progress.getAttribute("aria-valuenow"), 10)
  }
  // progress update
  sendMessage(msg)
}

function updatePlay() {
  const msg = {
    "type": "play",
    "value": !play.classList.contains("playing")
  }
  sendMessage(msg)
}

function panelModified() {
  title = document.querySelector(".playbackSoundBadge__titleContextContainer > div > a")
  title = title.getAttribute("title")
  if (title == last_title) {
    // Same title, play button has been triggered
    updatePlay()
  } else {
    // Not the same title, big update
    update()
    last_title = title
  }
}

function updateEventListener() {
  progress.addEventListener("DOMAttrModified", progressModified);
  panel.addEventListener("DOMAttrModified", panelModified)
}


function sendMessage(msg) {
  webSocket.send(JSON.stringify(msg))
}

function update() {
  updateData()
  const msg = {
    "type": "update",
    "image": image,
    "title": title,
    "user": user,
    "valuetext": progress.getAttribute("aria-valuetext"),
    "valueint": parseInt(progress.getAttribute("aria-valuenow"), 10),
    "playing": play.classList.contains("playing")
  }
  sendMessage(msg)
}

webSocket.onopen = function (event) {
  console.log("SOCKET OPEN")
  sendMessage({ "type": "connect" })
  console.log("1")
  updateData();
  console.log("2")
  updateEventListener();
  console.log("3")
  update();
  console.log("4")
};

webSocket.onmessage = function (event) {
  update();
}