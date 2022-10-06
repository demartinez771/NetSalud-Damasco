<script>
import axios from 'axios';

export default {
  data: function () {
    return {
      usuario: {
        username: "",
        password: "",
        perfil: "",
        nombre: "",
        apellido: "",
        celular: "",
        genero: "",
      }
    }
  },

  methods: {
    registroUsuario: function () {
      axios
        .post("https://netsalud-be-123.herokuapp.com/usuario/", this.usuario, {
          headers: {},
        },console.log(this.usuario))
        .then((result) => {
          let dataSignUp = {
            username: this.usuario.username,
            token_acess: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("registroUsuario", dataSignUp),alert("Usuario Registrado exitosamente!")
        },console.log("entro al then"))
        .catch((error) => {
          console.log(error);
          alert("Error: Fallo en el Registro Usuario");
        });
    }
  }
}
</script>

<template>
  <div id="rp" class="registro-usuario">
    <main>
      <form v-on:submit.prevent="registroUsuario">
        <div>
          <label>Username:</label>
          <input
            type="text"
            v-model="usuario.username"
            id="username"
            required
          />
        </div>

        <div>
          <label>Password:</label>
          <input
            type="password"
            v-model="usuario.password"
            id="password"
            required
          />
        </div>

        <div>
          <label>Perfil:</label>
          <select v-model="usuario.perfil" id="perfil">
            <option value="Personal de salud">Personal de salud</option>
            <option value="Paciente">Paciente</option>
            <option value="Auxiliar">Auxiliar</option>
          </select>
        </div>

        <div>
          <label>Nombre:</label>
          <input type="text" v-model="usuario.nombre" id="nombre" required />
        </div>

        <div>
          <label>Apellido:</label>
          <input
            type="text"
            v-model="usuario.apellido"
            id="apellido"
            required
          />
        </div>

        <div>
          <label>Celular:</label>
          <input
            type="tel"
            v-model="usuario.celular"
            id="celular"
            required
            minlength="7"
            maxlength="12"
          />
        </div>

        <div>
          <label>Genero:</label>
          <select v-model="usuario.genero" id="genero">
            <option value="M">M</option>
            <option value="F">F</option>
          </select>
          <br />
        </div>

        <button type="submit">Registrar</button>
      </form>
    </main>
  </div>
</template>

<style>
form label {
  display: inline-flexbox;
  width: 130px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  text-align: center;
  border-radius: 10px;
  color: #0d0e0d;
}

.registro-usuario {
  margin-top: 50px;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 400px;
  height: 600px;
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

select {
  width: 300px;
  height: 30px;
  display: block;
  background: #fafafa;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;
  border-radius: 10px;
  color: #070707;
}

form input {
  width: 300px;
  height: 25px;
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
  height: 30px;
  background: #2e2d4d;
  border-radius: 10px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 0px;
  text-align: center;
  color: #fafafa;
}
</style>
