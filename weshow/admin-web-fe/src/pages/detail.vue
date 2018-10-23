<template>
    <kw-layout>
        <div class="header">
            <span style="float: left; margin-left: 20px"><a href="javascript:history.back(-1)"><img src="../../static/left.png"></a></span>
            <span>{{ tv }}<span>
        </div>
        <div class="content">
            <h1>{{ apiData.name }}</h1>
            <h2>发布时间：{{ apiData.time }}</h2>
            <div>
                <video class="video-class" controls="controls" :src="apiData.video"></video>
            </div>
        </div>
    </kw-layout>
</template>

<script>
    export default {
        data() {
            return {
                url: this.api + '/weshow/',
                tv: '',
                id: '0',
                apiData: {}
            };
        },

        mounted() {
        },

        activated() {
            if (this.$route.query.tv) {
                this.tv = this.$route.query.tv;
            }
            if (this.$route.query.id) {
                this.id = this.$route.query.id;
            }
            this.search();
        },

        methods: {
            search() {
                this.$http.get(this.url + '?tv=' + this.tv + '&id=' + this.id).then((response) => {
                    this.apiData = response.data.results;
                });
            }
        }
    }
</script>

<style>
    .header {
        height: 90px;
        background: #1d6cb3;
        color: #fff;
        position: relative;
        line-height: 0.9rem;
        text-align: center;
        font: 0.33rem "Microsoft Yahei", "黑体";
    }

    .header span {
        line-height: 90px;
    }

    .video-class {
        width: 100%;
        height: 100%;
    }
</style>
