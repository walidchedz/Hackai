let user_id = localStorage.getItem("uid");

if(!user_id){
    user_id = Math.random().toString(36).substring(7);
    localStorage.setItem("uid", user_id);
}

async function send(){

    let msg = document.getElementById("msg").value;

    document.getElementById("chat").innerHTML +=
        `<div class="msg user">${msg}</div>`;

    let res = await fetch("/api/chat",{
        method:"POST",
        body: JSON.stringify({
            text: msg,
            user_id: user_id
        })
    });

    let data = await res.json();

    document.getElementById("chat").innerHTML +=
        `<div class="msg bot">${data.body.response}</div>`;
}
