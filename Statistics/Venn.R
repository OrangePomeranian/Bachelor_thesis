qbinom(0.95,12,0.5) 


qbinom(0.05,12,0.5) 
1 -



?qbinom
library(ggvenn)
#install.packages('ggVennDiagram')
#install.packages("gridExtra")     
library("gridExtra")  
library('ggVennDiagram')   
# use list as an input

walidacja_delecje_CNV <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/walidacja_razem_CNV_delecje_Venn.txt")
walidacja_delecje_Pin <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/walidacja_razem_Pin_delecje_Venn.txt")
walidacja_duplikacje_CNV <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/walidacja_razem_CNV_duplikacje_Venn.txt")
walidacja_duplikacje_Pin <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/walidacja_razem_Pin_duplikacje_Venn.txt")
Pindel_duplikacje <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/Pindel_razem_duplikacje_Venn.txt")
Pindel_delecje <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/Pindel_razem_delecje_Venn.txt")
CNVnator_duplikacje <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/CNVnator_razem_duplikacje_Venn.txt")
CNVnator_delecje <- read.csv("/Users/daria/Desktop/Dane_licencjat/Venn/CNVnator_razem_delecje_Venn.txt")


Pindel_delecje = Pindel_delecje$X0
Pindel_duplikacje  = Pindel_duplikacje$X0
CNVnator_duplikacje = CNVnator_duplikacje$X0
CNVnator_delecje = CNVnator_delecje$X0

walidacja_delecje_CNV = walidacja_delecje_CNV$X0
walidacja_delecje_Pin = walidacja_delecje_Pin$X0
walidacja_duplikacje_CNV = walidacja_duplikacje_CNV$X0
walidacja_duplikacje_Pin = walidacja_duplikacje_Pin$X0

x <-list('C++'= c(9,3,5,2),'Java'=c(7,8,4,3), 'Python'=c(11,2,4,5,8),'Ruby'=c(3,8))

y <- list('Pindel' = Pindel_delecje, 'Walidacja' = walidacja_delecje_Pin)
y <- list('CNVnator' = CNVnator_delecje, 'Walidacja' = walidacja_delecje_CNV )
y <- list('CNVnator' = CNVnator_duplikacje , 'Walidacja' = walidacja_duplikacje)
# creating Venn diagram and displaying 
# all sets

walidacja_delecje = append(walidacja_delecje_CNV , walidacja_delecje_Pin)
y <- list('Pindel' = Pindel_delecje,'CNVnator' =  CNVnator_delecje ,'Walidacja' = walidacja_delecje)
ggVennDiagram(y)

# ------------------------------------------------------------------------------
walidacja_duplikacje = append(walidacja_duplikacje_CNV , walidacja_duplikacje_Pin)
x <- list('Pindel' = Pindel_duplikacje,'Walidacja' = walidacja_duplikacje )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
              edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie walidacji dla duplikacji")

# ------------------------------------------------------------------------------
walidacja_duplikacje = append(walidacja_duplikacje_CNV , walidacja_duplikacje_Pin)
x <- list('CNVnator' = CNVnator_duplikacje,'Walidacja' = walidacja_duplikacje )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie walidacji dla duplikacji")



# ------------------------------------------------------------------------------
walidacja_delecje = append(walidacja_delecje_CNV , walidacja_delecje_Pin)
x <- list('Pindel' = Pindel_delecje,'Walidacja' = walidacja_delecje )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie walidacji dla delecji")

# ------------------------------------------------------------------------------
walidacja_delecje = append(walidacja_delecje_CNV , walidacja_delecje_Pin)
x <- list('CNVnator' = CNVnator_delecje,'Walidacja' = walidacja_delecje )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie walidacji dla delecji")






# ------------------------------------------------------------------------------
#walidacja_duplikacje = append(walidacja_duplikacje_CNV , walidacja_duplikacje_Pin)
x <- list('Pindel' = Pindel_duplikacje,'CNVnator' =  CNVnator_duplikacje ,'Walidacja' = walidacja_duplikacje)
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie walidacji dla duplikacji")
# ------------------------------------------------------------------------------
walidacja_delecje = append(walidacja_delecje_CNV , walidacja_delecje_Pin)
y <- list('Pindel' = Pindel_delecje,'CNVnator' =  CNVnator_delecje ,'Walidacja' = walidacja_delecje)

y = ggVennDiagram(y, label = c('count'), label_geom = c( 'label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3,  show.legend = F)

y = grid.arrange(y, top = "Porównanie walidacji dla delecji")



# ------------------------------------------------------------------------------
CNVnator = sample(c(1:4850))
Pindel = sample(c(2611:71462))

#walidacja_duplikacje = append(CNVnator , Pindel)
x <- list('Pindel' = Pindel,'CNVnator' = CNVnator )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie wspólnych wykrytych CNV dla duplikacji")

CNVnator = sample(c(1:10866))
Pindel = sample(c(7646:854756))

#walidacja_delecje = append(CNVnator , Pindel)
x <- list('Pindel' = Pindel,'CNVnator' = CNVnator )
x = ggVennDiagram(x, label = c('count'), label_geom = c('label', 'text'), label_color = "black", label_size = 4, label_txtWidth = 20, label_percent_digit = 1, 
                  edge_size = 1, edge_lty = 'solid', label_alpha = 0.4, set_size = 3, title = 'abx')

grid.arrange(x, top = "Porównanie wspólnych wykrytych CNV dla delecji")


