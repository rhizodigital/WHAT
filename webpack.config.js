const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const projectBase = "core";

const options = {
    entry: {
        main: './static_src/js/main.js',
    },
    output: {
        path: path.resolve(`./${projectBase}/static/`),
        filename: 'js/[name].js',
        publicPath: '/static/',
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/[name].css',
        }),
    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'postcss-loader'
                ],
            },
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                }
            }
        ]
    },
    devServer: {
        hot: false,
        proxy: {
            '*': 'http://127.0.0.1:8000',
        },
    },
};

module.exports = options;