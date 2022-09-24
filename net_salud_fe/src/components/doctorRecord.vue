<script>
export default {
  name: "MyComponen2",
  data() {
    return {
      subtitulo: "soy la verga",
    };
  },
  props: {
    title: '',
  },
};
</script>

<template>
  <div>
    <h1>Este es Mi componente</h1>
    <h2>{{ this.title }}</h2>
  </div>
</template>
