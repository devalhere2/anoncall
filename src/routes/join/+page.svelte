<script>
    import axios from "axios";
    let isPrivate = false;
    let username;
    let password;
    let serverId;
    async function joinServer() {
        if (isPrivate == false) {
            password = null
        } else if (isPrivate == true && password == null){
            alert("Please Enter Password")
            return
        }
        if (serverId == null){
            alert("Please Enter Served Id")
            return
        }
        await axios
            .post("http://localhost:8000/join", {
                username,
                serverId,
                password,
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err);
            });
    }
</script>

<main>
    <h2>Join Server:</h2>
    <input
        type="text"
        placeholder="Enter Username"
        bind:value={username}
    />
    <br />
    <input
        type="text"
        placeholder="Enter Server Id"
        bind:value={serverId}
    />
    <br />
    <input type="checkbox" id="private" bind:checked={isPrivate} />
    <label for="private">Private</label>
    <br />
    {#if isPrivate}
        <input
            type="password"
            placeholder="Enter Password"
            bind:value={password}
        />
        <br />
    {/if}
    <button on:click={joinServer}>Join</button>
</main>

<style lang="scss">
    main {
        margin: 10px;
        padding: 10px;
        border: 2px solid black;
        width: fit-content;
        background-color: wheat;
        * {
            margin: 2px;
            font-family: "Courier New", Courier, monospace;
            padding: 5px;
            font-weight: bold;
        }
    }
</style>
