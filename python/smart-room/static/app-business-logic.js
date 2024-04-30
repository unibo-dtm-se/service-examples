/*
 * Business logic of the web app 
 */

async function doLockRequest() {
    await fetch('http://localhost:8080/lock',{
      method: 'POST',
    })
    console.log("locked")
}

async function doTurnOnRequest() {
  const lightId = document.getElementById("lightId").value
  await fetch('http://localhost:8080/lights/' + lightId + '/turnOn',{ 
    method: 'POST' 
  })
  console.log("turned on ok")
}

async function doGetStateRequest() {
  const lightId = document.getElementById("lightId").value
  const response = await fetch('http://localhost:8080/lights/' + lightId + '/state',{ 
    method: 'GET' 
  })
  const jsonContent = await response.json()
  document.getElementById("state").innerHTML = jsonContent.state
  console.log("get state ok")
}

