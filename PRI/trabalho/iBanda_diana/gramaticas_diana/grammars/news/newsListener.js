// Generated from news.g4 by ANTLR 4.5.1
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by newsParser.
function newsListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

newsListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
newsListener.prototype.constructor = newsListener;

// Enter a parse tree produced by newsParser#newspaper.
newsListener.prototype.enterNewspaper = function(ctx) {
};

// Exit a parse tree produced by newsParser#newspaper.
newsListener.prototype.exitNewspaper = function(ctx) {
};


// Enter a parse tree produced by newsParser#news.
newsListener.prototype.enterNews = function(ctx) {
};

// Exit a parse tree produced by newsParser#news.
newsListener.prototype.exitNews = function(ctx) {
};


// Enter a parse tree produced by newsParser#titles.
newsListener.prototype.enterTitles = function(ctx) {
};

// Exit a parse tree produced by newsParser#titles.
newsListener.prototype.exitTitles = function(ctx) {
};


// Enter a parse tree produced by newsParser#title.
newsListener.prototype.enterTitle = function(ctx) {
};

// Exit a parse tree produced by newsParser#title.
newsListener.prototype.exitTitle = function(ctx) {
};


// Enter a parse tree produced by newsParser#topics.
newsListener.prototype.enterTopics = function(ctx) {
};

// Exit a parse tree produced by newsParser#topics.
newsListener.prototype.exitTopics = function(ctx) {
};


// Enter a parse tree produced by newsParser#topic.
newsListener.prototype.enterTopic = function(ctx) {
};

// Exit a parse tree produced by newsParser#topic.
newsListener.prototype.exitTopic = function(ctx) {
};


// Enter a parse tree produced by newsParser#body.
newsListener.prototype.enterBody = function(ctx) {
};

// Exit a parse tree produced by newsParser#body.
newsListener.prototype.exitBody = function(ctx) {
};


// Enter a parse tree produced by newsParser#date.
newsListener.prototype.enterDate = function(ctx) {
};

// Exit a parse tree produced by newsParser#date.
newsListener.prototype.exitDate = function(ctx) {
};


// Enter a parse tree produced by newsParser#authors.
newsListener.prototype.enterAuthors = function(ctx) {
};

// Exit a parse tree produced by newsParser#authors.
newsListener.prototype.exitAuthors = function(ctx) {
};


// Enter a parse tree produced by newsParser#author.
newsListener.prototype.enterAuthor = function(ctx) {
};

// Exit a parse tree produced by newsParser#author.
newsListener.prototype.exitAuthor = function(ctx) {
};



exports.newsListener = newsListener;