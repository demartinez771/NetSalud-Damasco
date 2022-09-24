<script>
export default {
  name: "prueba",
  data() {
    return {
      subtitulo: "prueba",
    };
  },
  props: {
    title: '',
  },
};
</script>

<template>
  <div>
    <h1></h1>
    <h2>{{ this.title }}</h2>
  </div>
</template>
