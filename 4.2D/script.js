async function controlLight(room, button)
{
    let state;

    if (button.classList.contains("active"))
    {
        state = 0;

        button.classList.remove("active");
        button.textContent = "OFF";
    }
    else
    {
        state = 1;

        button.classList.add("active");
        button.textContent = "ON";
    }


    const response = await fetch("/control-light",
    {
        method: "POST",

        headers:
        {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(
        {
            room: room,
            state: state
        })
    });


    const result = await response.json();

    console.log(result);
}