// Generated from agenda.g4 by ANTLR 4.5.1
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by agendaParser.
function agendaListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

agendaListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
agendaListener.prototype.constructor = agendaListener;

// Enter a parse tree produced by agendaParser#agenda.
agendaListener.prototype.enterAgenda = function(ctx) {
};

// Exit a parse tree produced by agendaParser#agenda.
agendaListener.prototype.exitAgenda = function(ctx) {
};


// Enter a parse tree produced by agendaParser#event.
agendaListener.prototype.enterEvent = function(ctx) {
};

// Exit a parse tree produced by agendaParser#event.
agendaListener.prototype.exitEvent = function(ctx) {
};


// Enter a parse tree produced by agendaParser#title.
agendaListener.prototype.enterTitle = function(ctx) {
};

// Exit a parse tree produced by agendaParser#title.
agendaListener.prototype.exitTitle = function(ctx) {
};


// Enter a parse tree produced by agendaParser#desc.
agendaListener.prototype.enterDesc = function(ctx) {
};

// Exit a parse tree produced by agendaParser#desc.
agendaListener.prototype.exitDesc = function(ctx) {
};


// Enter a parse tree produced by agendaParser#local.
agendaListener.prototype.enterLocal = function(ctx) {
};

// Exit a parse tree produced by agendaParser#local.
agendaListener.prototype.exitLocal = function(ctx) {
};


// Enter a parse tree produced by agendaParser#time.
agendaListener.prototype.enterTime = function(ctx) {
};

// Exit a parse tree produced by agendaParser#time.
agendaListener.prototype.exitTime = function(ctx) {
};


// Enter a parse tree produced by agendaParser#start.
agendaListener.prototype.enterStart = function(ctx) {
};

// Exit a parse tree produced by agendaParser#start.
agendaListener.prototype.exitStart = function(ctx) {
};


// Enter a parse tree produced by agendaParser#end.
agendaListener.prototype.enterEnd = function(ctx) {
};

// Exit a parse tree produced by agendaParser#end.
agendaListener.prototype.exitEnd = function(ctx) {
};


// Enter a parse tree produced by agendaParser#startDate.
agendaListener.prototype.enterStartDate = function(ctx) {
};

// Exit a parse tree produced by agendaParser#startDate.
agendaListener.prototype.exitStartDate = function(ctx) {
};


// Enter a parse tree produced by agendaParser#startHour.
agendaListener.prototype.enterStartHour = function(ctx) {
};

// Exit a parse tree produced by agendaParser#startHour.
agendaListener.prototype.exitStartHour = function(ctx) {
};


// Enter a parse tree produced by agendaParser#endDate.
agendaListener.prototype.enterEndDate = function(ctx) {
};

// Exit a parse tree produced by agendaParser#endDate.
agendaListener.prototype.exitEndDate = function(ctx) {
};


// Enter a parse tree produced by agendaParser#endHour.
agendaListener.prototype.enterEndHour = function(ctx) {
};

// Exit a parse tree produced by agendaParser#endHour.
agendaListener.prototype.exitEndHour = function(ctx) {
};



exports.agendaListener = agendaListener;