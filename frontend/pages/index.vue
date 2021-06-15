<template>
  <div>
    <Header />
    <main class="container content-wrapper">
      <!-- Title -->
      <h1 class="title">Nxrth-x</h1>
      <!-- Posts -->
      <Post :post="leading_post" :main="true" />
      <div class="cards">
        <Post v-for="post in posts" :post="post" :key="post.id" />
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, error }) {
    try {
      const data = await $axios.$get("post/");

      const [leading_post, ...posts] = data;

      return {
        leading_post,
        posts,
      };
    } catch {
      error("Something went wrong. :(");
    }
  },
};
</script>

<style lang="scss" scoped>
@import "../scss/variables.scss";

main.content-wrapper {
  padding-bottom: 4rem;
}

h1.title {
  margin: 1rem 0;
  font-size: 4rem;

  @media (min-width: 600px) {
    font-size: 6rem;
  }

  @media (min-width: 900px) {
    font-size: 8rem;
  }
}

div.cards {
  margin-top: 2rem;

  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4rem;

  @media (max-width: 900px) {
    gap: 2rem;
    grid-template-columns: repeat(2, 1fr);
  }

  @media (max-width: 420px) {
    grid-template-columns: 1fr;
  }
}
</style>
