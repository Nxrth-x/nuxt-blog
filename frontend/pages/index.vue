<template>
  <div>
    <Header />
    <main class="container content-wrapper">
      <!-- Title -->
      <h1 class="title">Nxrth-x</h1>
      <!-- Main card -->
      <div class="main-card">
        <img :src="leading_post.thumbnail" :alt="leading_post.title" />
        <div>
          <span class="date">{{ leading_post.date }}</span>
          <h1>{{ leading_post.title }}</h1>
          <p>{{ leading_post.excerpt }}</p>
        </div>
      </div>
      <!-- Cards -->
      <div class="cards">
        <div class="card" v-for="(post, index) in posts" :key="index">
          <img :src="post.thumbnail" :alt="post.title" />
          <div>
            <span class="date">{{ post.date }}</span>
            <h1>{{ post.title }}</h1>
            <p>{{ post.excerpt }}</p>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    try {
      const data = await $axios.$get("http://localhost:8000/api/post/");

      console.log(data);

      return [];
    } catch {}
  },
  data: () => ({
    posts: [
      {
        date: "March 5, 2021.",
        title: "Being creative is not my virtue, it never was.",
        excerpt: "Something I've been saying since a long time ago",
        thumbnail: "https://dwinawan.com/blog/thumb_article10.jpg",
      },
      {
        date: "May 4, 2021.",
        title: "May the fourth be with you, lol.",
        excerpt: "Is that a reference to Star Wars? No way bro. xD",
        thumbnail: "https://dwinawan.com/blog/thumb_article8.jpg",
      },
      {
        date: "February 15, 2021.",
        title: "Being a fullstack is cool, isn't it?",
        excerpt:
          "Being a fullstack developer is hard, but it has some cool perks. xD",
        thumbnail: "https://dwinawan.com/blog/thumb_article7.jpg",
      },
      {
        date: "March 5, 2021.",
        title: "Being creative is not my virtue, it never was.",
        excerpt: "Something I've been saying since a long time ago",
        thumbnail: "https://dwinawan.com/blog/thumb_article10.jpg",
      },
      {
        date: "May 4, 2021.",
        title: "May the fourth be with you, lol.",
        excerpt: "Is that a reference to Star Wars? No way bro. xD",
        thumbnail: "https://dwinawan.com/blog/thumb_article8.jpg",
      },
      {
        date: "February 15, 2021.",
        title: "Being a fullstack is cool, isn't it?",
        excerpt:
          "Being a fullstack developer is hard, but it has some cool perks. xD",
        thumbnail: "https://dwinawan.com/blog/thumb_article7.jpg",
      },
    ],
    leading_post: this.posts[0],
  }),
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

div.main-card {
  display: none;
}

div.main-card,
div.card {
  cursor: pointer;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;

  transition: $transition;

  h1 {
    background: linear-gradient(90deg, $pink, $red, $orange);
    -webkit-text-fill-color: transparent;
    background-clip: text;

    filter: grayscale(1) brightness(0);

    transition: $transition;
  }

  img {
    border-radius: 0.5rem;
    width: 100%;
    object-fit: cover;
  }

  div {
    span {
      color: $gray;
      letter-spacing: 2px;
    }
  }

  &:hover {
    transform: scale(1.025);

    h1 {
      filter: grayscale(0) brightness(1);
    }
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

div.main-card {
  margin: 2rem 0;

  h1 {
    margin: 1rem 0;
    font-size: 3rem;
    line-height: 3.25rem;
    letter-spacing: -2px;
  }

  @media (min-width: 900px) {
    margin: 2rem 0 4rem 0;

    flex-direction: row;

    img {
      width: 48%;
    }
  }
}

div.card {
  gap: 1rem;

  h1 {
    margin: 0.5rem 0;
    font-size: 2rem;
    letter-spacing: -1px;
    line-height: 2.25rem;
  }
}
</style>
