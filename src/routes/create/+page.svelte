<script>
    import axios from "axios";
    let isPrivate = false;
    let username;
    let password;
    let serverId;
    async function createServer() {
        if (isPrivate == false) {
            password = null
        } else if (isPrivate == true && password == null){
            alert("Please Enter Password")
            return
        }
        await axios
            .post("http://localhost:8000/create", {
                username,
                serverId,
                password,
            })
            .then((res) => {
                console.log(res.data)
            })
            .catch((err) => {
                console.log(err);
            });
    }
</script>

<main>
    <h2>Create Server:</h2>
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
    <button on:click={createServer}>Create</button>
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
