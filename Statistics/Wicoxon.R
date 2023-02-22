CNVnator<- read.csv("/Users/daria/Desktop/Dane_licencjat/CNVnator/del_S4389Nr1.txt", sep = ' ')
Pindel <- read.csv("/Users/daria/Desktop/Dane_licencjat/Pindel/M_Nr1.D.txt", sep = ',')
CNVnator = CNVnator$dlug
Pindel = Pindel$dlug
wilcox.test(CNVnator, Pindel, paired = F, alternative = 'two.sided')

delecje = read.csv("/Users/daria/Desktop/Dane_licencjat/Walidacja_1/delecje.txt", sep = ' ')
duplikacje = read.csv("/Users/daria/Desktop/Dane_licencjat/Walidacja_1/duplikacje.txt", sep = ' ')

# test znaków
for (index in  (1:12)){
  CNVnator<- read.csv(delecje$path[index], sep = ' ')
  Pindel <- read.csv(delecje$Pindel[index], sep = ',')
  print(nrow(Pindel) - nrow(CNVnator))
}

for (index in  (1:12)){
  CNVnator<- read.csv(duplikacje$path[index], sep = ' ')
  Pindel <- read.csv(duplikacje$Pindel[index], sep = ',')
  print(nrow(Pindel) - nrow(CNVnator))
}
# normalnosc

#install.packages('nortest')
library(nortest)
CNVnator = data.frame()
Pindel = data.frame()

for (index in  (1:12)){
  
  CNVnator1 <- read.csv(delecje$path[index], sep = ' ')
  Pindel1 <- read.csv(delecje$Pindel[index], sep = ',')
  CNVnator = rbind(CNVnator, CNVnator1)
  Pindel = rbind(Pindel, Pindel1)
}

x = lillie.test(CNVnator$dlug)
if (x$p.value < 0.05){
  print(lillie.test(CNVnator$dlug))
  print('Odrzucamy H0')
}else{
  print('przyjmujemy H0')
} 
print(x$p.value)

x = lillie.test(Pindel$dlug)
if (x$p.value < 0.05){
  print(lillie.test(Pindel$dlug))
  print('Odrzucamy H0')
}else{
  print('przyjmujemy H0')
} 
print(x$p.value)






for (index in  (1:12)){
  CNVnator<- read.csv(delecje$path[index], sep = ' ')
  Pindel <- read.csv(delecje$Pindel[index], sep = ',')
  x = lillie.test(CNVnator$dlug)
  if (x$p.value < 0.05){
    print(lillie.test(CNVnator$dlug))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
  } 
  print(x$p.value)
  x = lillie.test(Pindel$dlug)
  if (x$p.value < 0.05){
    print(lillie.test(Pindel$dlug))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
  } 
  print(x$p.value)
}

for (index in  (1:12)){
  CNVnator<- read.csv(delecje$path[index], sep = ' ')
  Pindel <- read.csv(delecje$Pindel[index], sep = ',')
  x = lillie.test(CNVnator$dlug)
  if (x$p.value < 0.05){
    print(lillie.test(CNVnator$dlug))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
  } 
  print(x$p.value)
  x = lillie.test(Pindel$dlug)
  if (x$p.value < 0.05){
    print(lillie.test(Pindel$dlug))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
  } 
  print(x$p.value)
}
# wszędzie H0



# Wilcoxon
z = data.frame()
for (index in  (1:12)){
  CNVnator<- read.csv(delecje$path[index], sep = ' ')
  Pindel <- read.csv(delecje$Pindel[index], sep = ',')
  x = wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' )
  y = p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug))
  z = rbind(z,y)
  if (x$p.value < 0.05){
    #print(wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' ))
    print(p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug)))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
    print(p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug)))
  } 
  #print(x$p.value)
  #print(wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' ))

}
numbers = 1:12
numbers = data.frame(numbers)
del = z

z = data.frame()
for (index in  (1:12)){
  CNVnator<- read.csv(duplikacje$path[index], sep = ' ')
  Pindel <- read.csv(duplikacje$Pindel[index], sep = ',')
  y = p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug))
  z = rbind(z,y)
  x = wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' )
  if (x$p.value < 0.05){
    print(p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug)))
    #print(wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' ))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
    print(p.adjust(x$p.value, method = p.adjust.methods, n = length(CNVnator$dlug)))
  } 
  #print(x$p.value, index)
}
dup = z
numbers = 1:12
numbers = data.frame(numbers)


par(mfrow=c(2,1))
plot(numbers$numbers, del$X0,
     main = "Wartość p dla testu Wilcoxona Manna-Withneya",
     xlab = "",
     ylab = "Numer osobnika",
     col="blue",
     pch = 20,
     cex = 1.5)
set(xlabel=None)
plot(numbers$numbers, dup$X0,
     main = "Wartość p dla testu Wilcoxona Manna-Withneya",
     xlab = "Wartość p",
     ylab = "Numer osobnika",
     col="blue",
     pch = 20,
     cex = 1.5)

library(ggplot2)
del$numbers = numbers$numbers
del$program = 'delecje'
dup$numbers = numbers$numbers
dup$program = 'duplikacje'

finish = rbind(del,dup)

print(max(finish$X0))
ggplot(finish, aes(y = X0, x = numbers, group = program, color = program))+ 
  theme(plot.title = element_text(hjust = 0.5)) +
  ggtitle("Wartość p dla testu Wilcoxona Manna-Withneya")  +
  ylab("Wartość p") +
  xlab("Numer osobnika") + 
  geom_point(size=6, aes(shape = program)) +
  scale_x_continuous(breaks = seq(0, 12, by = 1)) +
  theme(legend.title = element_blank())





bonferroni(x$p.value, 0.05, silent=FALSE)
pairwise.t.test(CNVnator$dlug, Pindel$dlug, p.adjust = "bonferroni")
#pairwise.t.test(x, g, p.adjust.method=”bonferroni”)

for (index in  (1:12)){
  CNVnator<- read.csv(delecje$path[index], sep = ' ')
  Pindel <- read.csv(delecje$Pindel[index], sep = ',')
  x = pairwise.t.test(CNVnator$dlug, Pindel$dlug, p.adjust.method = 'bonferroni')
  #x = wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' )
  if (x$p.value < 0.05){
    #print(wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' ))
    print('Odrzucamy H0')
  }else{
    print('przyjmujemy H0')
  } 
  print(x$p.value)
  #print(wilcox.test(CNVnator$dlug, Pindel$dlug, paired = F, alternative = 'two.sided' ))
  
}

# -------
for (index in  (1:12)){
Pindeldel <- read.csv(delecje$Pindel[index], sep = ',')
Pindeldup <- read.csv(duplikacje$Pindel[index], sep = ',')
print(nrow(Pindeldel) - nrow(Pindeldup))
}