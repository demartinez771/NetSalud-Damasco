<script>
import axios from 'axios';

export default {
  data: function () {
    return {
      PersonalSalud: {
        documento: "",
        rol: "",
        especialidad: "",
        username: "",
      }
    }
  },

  methods: {
    registroPSalud: function () {
      axios.post(
        "https://netsalud-be.herokuapp.com/pSalud/",
        this.pSalud,
        { headers: {} }
      )

        .then((result) => {
          alert("Personal de Salud Registrado exitosamente!")
          this.$emit('registroPSalud')
        })
        .catch((error) => {
          console.log(error);
          alert("Upps No se ha podido registrar el Personal de Salud :(")
        })
    }
  }
}

</script>
    
<template>
  <div id="rp" class="registro-pSalud">
    <main>
      <form v-on:submit.prevent="registroPSalud">
        <div>
          <label>Documento:</label>
          <input type="text" v-model="PersonalSalud.documento" id="documento" required>
        </div>

        <div>
          <label>Rol:</label>
          <input type="text" v-model="PersonalSalud.rol" id="rol" required>
        </div>

        <div>
          <label>Especialidad:</label>
          <input type="text" v-model="PersonalSalud.especialidad" id="especialidad" required>
        </div>

        <div>
          <label>Username:</label>
          <input type="text" v-model="PersonalSalud.username" id="username" required>
        </div>

        <button type="submit">Registrar</button>

      </form>
    </main>


  </div>
</template>
    
<style>
form label {
  font-size: 17px;
  display: inline-flexbox;
  width: 110px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;
  border-radius: 10px;
  color: #0d0e0d;
}

.registro-pSalud {
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