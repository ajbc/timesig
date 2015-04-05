
library(ggplot2)
library(reshape2)
setwd('<absolute path>/explore/')

dat.book <- read.csv('pro/all_docs.csv')
dat.time <- read.csv('dat/time_indicators.csv')
dat.time$word <- tolower(dat.time$word)
dat.time <- dat.time[dat.time$word %in% dat.book$anchor,]
dat.time$color.idx <- 0
dat.time[dat.time$level=="year",]$color.idx <- seq(nrow(dat.time[dat.time$level=="year",]))
dat.time[dat.time$level=="month",]$color.idx <- seq(nrow(dat.time[dat.time$level=="month",]))
dat.time[dat.time$level=="week",]$color.idx <- seq(nrow(dat.time[dat.time$level=="week",]))
dat.time[dat.time$level=="day",]$color.idx <- seq(nrow(dat.time[dat.time$level=="day",]))
dat.time[dat.time$level=="hour",]$color.idx <- seq(nrow(dat.time[dat.time$level=="hour",]))
dat.time[dat.time$level=="minute",]$color.idx <- seq(nrow(dat.time[dat.time$level=="minute",]))


dat <- merge(dat.book, dat.time, by.x="anchor", by.y="word")
dat$level <- factor(dat$level, levels=c("minute", "hour", "day", "week", "month", "year"))

p <- ggplot(dat, aes(x=index, y=level, color=factor(color.idx),label=anchor)) + geom_text(angle=90)
p <- p + facet_wrap(~doc, scales="free")
p <- p + theme(legend.position="none") + xlab("word index") + ylab("")
p

ggsave(file="fig/all_docs.pdf",width=40, height=20)
