<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Control Panel</title>
</head>
<body>
    <div class="wrapper">
        <form action="/start_bot" method="post">
            <button class='start' type="submit">Start Bot</button>
        <form action="/stop_bot" method="post">
            <button class='stop' type="submit">Stop Bot</button>
        <form action="/get_diversity" name="get_diversity" id='get_diversity'method="post">
            <select class="i-3" name="model">
                <option value="" disabled selected>Choose the diversity</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select>
        <form action="/" method="post">
            <input class="i-2" type="text" name="Tokens" placeholder="Maximum tokens (max: 60) ">
        <form action="/" method="post">
        <select class="i-3" name="model" placeholder="Choose a model">
            <option value="" disabled selected>Choose the model</option>
            <option value="text-davinci-001">text-davinci-001</option>
            <option value="text-davinci-002">text-davinci-002</option>
            <option value="text-davinci-003">text-davinci-003</option>
        </select>
        <form action="/" method="post">
            <input class="i-4 "type="text" name="prompt" placeholder="Choose the prompt eg. what the bot should do ">
        <p class="status-text">Bot is running...</p>
        <p class="status-text-2">Bot has stopped...</p>
    </div>
    <div class="wrapper-2">
        <h4>Built by cop6567 on GitHub</h4>
        

    </div>
</body>
</html>

<style>
    body {
        display: flex;
        background-color: rgb(4, 32, 65);
        justify-content: space-between;

    }

    .wrapper-2 {
        float: right;
        color: aliceblue;
        font-family: Arial, Helvetica, sans-serif;
        
    }

    .wrapper {
        display: inline-block;

    }

    button {
        width: 200px;
        height: 50px;
        font-size: 20px;
        border: none;
    }
    
    .start,
    .stop {
        display: block;
        margin-top: 10px;
        color: aliceblue;
        border-radius: 10px;
        background-color: brown;
        margin-left: 20px;
        letter-spacing: 1px;
    }

    .start:hover,
    .stop:hover {
        background-color: red;
        transition: 0.3s;

    }

    .start:hover {
        background-color: greenyellow;
    }

    .start {
        background-color: green;
    }

    select {
        height: 43px !important;
        width: 315px !important;
        padding-right: 30px !important;

    }
    .status-text-2
    .status-text,
    select,
    input {
        width: 290px;
        height: 20px;
        padding: 10px;
        margin-top: 20px;
        margin-left: 20px;
        display: block;

    }
    .status-text-2,
    .status-text {
        margin-top: 10px;
        font-size: 30px;
        font-family: Arial, Helvetica, sans-serif;
        letter-spacing: 3px;
        color: green;
        display: none;
    }

    .status-text-2 {
        color: red;
    }

   

    
</style>


<script>
    const startButton = document.querySelector('.start');
    const statusText = document.querySelector('.status-text');

    startButton.addEventListener('click', () => {
        // Show the status text
        statusText.style.display = 'block';
    });


    const stopButton = document.querySelector('.stop');
    const statusText2 = document.querySelector('.status-text-2');

    stopButton.addEventListener('click', () => {
        // Show the status text
        statusText2.style.display = 'block';
    });
</script>
