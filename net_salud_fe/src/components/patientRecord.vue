<script>
import axios from 'axios';

export default {
  data: function () {
    return {
      paciente: {
        documento: "",
        fecha_nac: "",
        ciudad: "",
        direccion: "",
        username: "",
        pSalud_documento: "",
      }
    }
  },

  methods: {
    registroPaciente: function () {
      axios.post(
        "https://netsalud-be.herokuapp.com/paciente/",
        this.paciente,
        { headers: {} }
      )

        .then((result) => {
          alert("Paciente Registrado exitosamente!")
          this.$emit('registroPaciente')
        })
        .catch((error) => {
          console.log(error);
          alert("Upps No se ha podido registrar el Paciente :(")
        })
    }
  }
}

</script>

<template>
  <div id="rp" class="registro-paciente">
    <main>
      <form v-on:submit.prevent="registroPaciente">
        <div>
          <label>Documento:</label>
          <input type="text" v-model="paciente.documento" id="documento" required>
        </div>

        <div>
          <label>Fecha de Nacimiento:</label>
          <input type="date" v-model="paciente.fecha_nac" id="fecha_nac" required>
        </div>

        <div>
          <label>Ciudad:</label>
          <input type="text" v-model="paciente.ciudad" id="ciudad" required>
        </div>

        <div>
          <label>Dirección:</label>
          <input type="text" v-model="paciente.direccion" id="direccion" required>
        </div>

        <div>
          <label>Username:</label>
          <input type="text" v-model="paciente.username" id="username" required>
        </div>

        <div>
          <label>Documento Personal de Salud:</label>
          <input type="text" v-model="paciente.pSalud_documento" id="pSalud_documento" required>
          <br>
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

.registro-paciente {
  margin-top: 50px;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 747px;
  height: 648px;
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
