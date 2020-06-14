const socket = io()
document.getElementById("button").addEventListener("click", function(e) {
    /* mess = document.getElementById("mess").value
     let route = window.location + mess
     console.log(route)*/



    e.preventDefault()
    const msj = document.getElementById("message").value
    const date = new Date()

    const hora = date.getHours() + ":" + date.getMinutes()

    const fecha = {
        "day": date.getDate(),
        "month": date.getMonth() + 1,
        "year": date.getFullYear(),
        "hour": date.getHours(),
        "minute": date.getMinutes()
    }

    const info = {
        "user": window.location.href.split("/")[4],
        "fecha": fecha,
        "message": msj
    }
    socket.send(info)

    document.getElementById("message").value = ""
})

socket.on("message", function(info) {
    console.log(info)

    const container = document.getElementById("container")

    const element = document.createElement("div")

    var color = "",
        align = ""
    if (info.user == window.location.href.split("/")[4]) {
        color = "primary"
        align = "right"
    } else {
        color = "light"
        align = "left"
    }



    element.innerHTML = `
            <div class="card text-${align} mb-4 bg-${color}">
                <div class="card-body">
                    <strong>From </strong>: ${info.user}
                    <strong>At </strong>: ${info.fecha.hour+":"+info.fecha.minute}
                    <strong>Message </strong>: ${info.message}
                </div>
            </div>`

    container.appendChild(element)

})