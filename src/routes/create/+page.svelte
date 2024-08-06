<script>
    import axios from "axios";
    import { goto } from "$app/navigation";

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
                goto(`/room/${res.data.serverId}`)
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
        placeholder="Enter Username #"
        bind:value={username}
    />
    <br />
    <input
        type="text"
        placeholder="Enter Server Id #"
        bind:value={serverId}
    />
    <br />
    <input type="checkbox" id="private" bind:checked={isPrivate} />
    <label for="private">Private</label>
    <br />
    {#if isPrivate}
        <input
            type="password"
            placeholder="Enter Password *"
            bind:value={password}
        />
        <br />
    {/if}
    <span>
        <button on:click={createServer}>Create</button>
        <div># Optional, * Required</div>
    </span>
</main>

<style lang="scss">
    main {
        margin: 10px;
        padding: 10px;
        border: 2px solid black;
        width: fit-content;
        background-color: wheat;
        span {
            display: flex;
            align-items: center;
            font-size: 10px;
            justify-content: space-between;
            padding: 0;
            margin: 0;
            div{
                background-color: orange
            }
        }
        * {
            margin: 2px;
            font-family: "Courier New", Courier, monospace;
            padding: 5px;
            font-weight: bold;
        }
    }
</style>
