<template>
    <div id="rp" class="registro-familiar">
        <main>
            <form v-on:submit.prevent="logIn">
                <div>
                    <label>Username:</label>
                    <input type="text" v-model="usuario.username" id="username" required>
                </div>

                <div>
                    <label>Password:</label>
                    <input type="password" v-model="usuario.password" id="password" required>
                </div>

                <button type="submit">Iniciar Sesión</button>

            </form>
        </main>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data: function () {
        return {
            usuario: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        logIn: function () {
            axios.post("https://netsalud-be-123.herokuapp.com/login/",
                this.usuario, { header: {} })
                .then((result) => {
                    console.log(result);
                    let dataLogIn = {
                        username: this.usuario.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit(newFunction(), dataLogIn)

                  function newFunction() {
                    return 'completedLogIn';
                  }
                },alert("ingreso correctamente")).catch((error) => {
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas");
                }
                );
        }
    }
}
</script>
  
<style>
form label {
    font-size: 17px;
    display: inline-flexbox;
    width: 130px;
    font-family: "Kanit";
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 45px;
    text-align: center;
    border-radius: 10px;
    color: #0d0e0d;
}

.registro-familiar {
    margin-top: 50px;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

form {
    width: 600px;
    height: 500px;
    margin: 0 0 0 40px;
    flex-direction: column;
    padding: 10px;
    display: flex;
    background: #e3f2fd;
    border-radius: 20px;
    justify-content: space-evenly;
    align-items: center;
    border: 5px solid #2e2d4d;
}


form input {
    width: 300px;
    height: 40px;
    display: block;
    background: #fafafa;
    font-family: "Kanit";
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 45px;
    text-align: center;
    border-radius: 10px;
    color: #050505;
}

button {
    width: 300px;
    height: 50px;
    background: #2e2d4d;
    border-radius: 10px;
    font-family: "Kanit";
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 45px;
    text-align: center;

    color: #fafafa;
}
</style>