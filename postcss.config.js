module.exports = ({ env }) => ({
    plugins: [
        require('tailwindcss'),
        require('./tailwind.config'),
        require('autoprefixer'),
        env === 'production' ? require('cssnano')({ preset: 'default',}) : false,
    ]
})