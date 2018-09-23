<template>
    <kw-layout>
        <div class="title">包含10年历史和自动站数据</div>
        <template v-for="item in apiData">
            <a :href="item.url" class="file-name">{{ item.name }}</a>
            <div class="file-info">------------ 更新时间:{{ item.time }} ------------ 文件大小:{{ item.size }}B</div>
            <br>
        </template>
    </kw-layout>
</template>

<script>
    export default {
        data() {
            return {
                url: this.api + '/excel/',
                apiData: [],
                date: ''
            };
        },

        mounted() {
        },

        activated() {
            if (this.$route.query.date) {
                this.date = this.$route.query.date;
            }
            this.search();
        },

        methods: {
            search() {
                this.$http.get(this.url + '?date=' + this.date).then((response) => {
                    this.apiData = response.data.results;
                });
            }
        }
    }
</script>

<style>
    a:-webkit-any-link {
        color: -webkit-link;
        cursor: pointer;
        text-decoration: underline;
    }

    .title {
        color: red;
        font-size: 48px;
        font-weight: bold;
        margin-top: 40px;
        display: block;
        margin-left: 50px;
    }

    .file-name {
        font-size: 24px;
        display: inline-block;
        margin-left: 50px;
        width: 270px;
    }

    .file-info {
        display: inline-block;
        font-size: 18px;
    }
</style>
