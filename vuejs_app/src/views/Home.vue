<template>
  <div class="home">
    <TextBox />
  </div>
</template>

<script>
// @ is an alias to /src
import TextBox from "@/components/TextBox.vue";

export default {
  name: "Home",
  components: {
    TextBox
  }
};
</script>
