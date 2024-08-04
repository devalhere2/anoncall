<script>
    import axios from "axios";
    let isPrivate = false;
    let username;
    let password;
    let serverId
</script>

<main>
    <h2>Create Server:</h2>
    <input type="text" name="" id="" placeholder="Enter Username" bind:value={username}/>
    <br />
    <input type="text" name="" id="" placeholder="Enter Server Id" bind:value={serverId}/>
    <br />
    <input type="checkbox" name="" id="private" bind:checked={isPrivate} />
    <label for="private">Private</label>
    <br>
    {#if isPrivate}
        <input type="password" name="" id="" placeholder="Enter Password" bind:value={password}/>
        <br>
    {/if}
    <button>Create</button>
</main>

<style lang="scss"> 
    main {
        *{
            margin: 2px;
            font-family: 'Courier New', Courier, monospace;
            padding: 5px;            
        }
        h2{
            text-decoration: underline;
        }
        button{
            background-color: orangered;
            color: wheat;
            font-size: 16px;
            font-weight: bold;
            width: 100px;
            border: 2px solid black;
            border-radius: 5px;
            transition: transform 200ms;
            &:active{
                
                transform: translate(2px,2px);
            }
        }
        margin: 10px;
        padding: 10px;
        border: 2px solid black;
        border-radius: 10px;
        width: 250px;
        background-color: wheat;
    }
</style>
