<template>
  <div id="app">
    <Header/>
    <router-view />

  </div>
</template>

<script>
import Header from "./components/Header";


export default {
  name: 'App',

  components: {
    Header
  }


}
</script>

<style>
  body {
    background: #76b852;
    background: linear-gradient(to left, #76b852, #8DC26F);
    font-family: "Roboto", sans-serif;
  }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }

  a {
    color: #ffffff;
    text-decoration: none;
  }

  .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  #header_logo {
    font-weight: 500;
    color: #ffffff;
    margin-left: 30px;
  }

  .nav_bar {
    width: 150px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 20px;
    color: #373737;
    margin-right: 30px;
  }

  .nav_link:hover {
    text-decoration: underline;
  }

  .search {
    width: 280px;
    position: relative;
    display: flex;
  }

  .searchTerm {
    width: 100%;
    border: 3px solid #489b1b;
    border-right: none;
    padding: 5px;
    height: 20px;
    border-radius: 5px 0 0 5px;
    outline: none;
    color: #9DBFAF;
    font-size: 18px;
  }

  .searchTerm:focus {
    color: #489b1b;
  }

  .searchButton {
    width: 80px;
    height: 36px;
    border: 1px solid #489b1b;
    background: #489b1b;
    text-align: center;
    color: #fff;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
    font-size: 20px;
  }

  .theatricals {
    max-width: 1440px;
    margin: 30px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .theatrical {
    max-width: 260px;
    max-height: 300px;
    background: #ffffff;
    font-size: 20px;
    margin: 15px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }

  .theatrical:hover {
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.5), 0 5px 5px 0 rgba(0, 0, 0, 0.5);
  }

  .poster_img {
    margin: 5px;
    width: 210px;
  }

  .theatrical_name {
    color: #292929;
  }

  footer {
    position: relative;
    bottom: 0;
    display: flex;
    justify-content: center;
  }

  @media screen and (max-device-width: 480px) and (orientation: portrait) {
    #header_logo {
      font-size: 60px;
    }

    .nav_bar {
      width: 300px;
      font-size: 40px;
    }

    .theatrical {
      max-width: 410px;
      max-height: 670px;
      font-size: 40px;
      margin: 15px;
    }

    .poster_img {
      width: 400px;
    }

    footer {
      font-size: 30px;
    }

    .search {
      width: 70%;
    }

    .searchTerm {
      height: 60px;
      font-size: 36px;
    }

    .searchButton {
      width: 80px;
      height: 76px;
      font-size: 40px;
    }
  }
</style>
