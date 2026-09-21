const express = require("express");
const axios = require("axios");

const app = express();

const BLYNK_TOKEN = "acTHCHEcIMwZQm0MiJRpT1RnV9f5jEBX";

app.use(express.json());

app.use(express.static(__dirname));


app.post("/control-light", async (req, res) =>
{
    const room = req.body.room;
    const state = req.body.state;

    let pin;


    if (room === "living room")
    {
        pin = "V0";
    }
    else if (room === "bathroom")
    {
        pin = "V1";
    }
    else if (room === "closet")
    {
        pin = "V2";
    }
    else
    {
        return res.status(400).json(
        {
            success: false,
            message: "Invalid room"
        });
    }


    try
    {
        await axios.get(
            `https://blynk.cloud/external/api/update?token=${BLYNK_TOKEN}&${pin}=${state}`
        );

        console.log(room, state);

        res.json(
        {
            success: true
        });
    }
    catch (error)
    {
        console.log("Blynk error");

        res.status(500).json(
        {
            success: false
        });
    }
});


app.listen(3000, () =>
{
    console.log("Server running at http://localhost:3000");
});