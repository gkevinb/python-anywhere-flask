module.exports = {
    outputDir: '../static',
    publicPath: process.env.NODE_ENV === 'production' ?
        '/static/' :
        '/'
}