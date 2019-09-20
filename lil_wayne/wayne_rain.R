library(ggplot2)
library(png)
library(grid)
library(EBImage)

my_data <- read.csv("Google_rainfall_data.csv")

# Import Lil' Wayne pic
img <- readPNG('lil_wayne_small.png')

# Sort out image rastering etc. -- code taken from this SO thread:
# http://stackoverflow.com/questions/27637455/display-custom-image-as-geom-point
RlogoGrob <- function(x, y, size, img) {
    rasterGrob(x = x, y = y, image = img, default.units = "native", height = size, 
               width = size)
}

GeomRlogo <- ggproto("GeomRlogo", Geom, draw_panel = function(data, panel_scales, 
                                                              coord, img, na.rm = FALSE) {
    coords <- coord$transform(data, panel_scales)
    ggplot2:::ggname("geom_Rlogo", RlogoGrob(coords$x, coords$y, coords$size, 
                                             img))
}, non_missing_aes = c("Rlogo", "size"), required_aes = c("x", "y"), default_aes = aes(size = 0.05), 
icon = function(.) {
}, desc_params = list(), seealso = list(geom_point = GeomPoint$desc), 
examples = function(.) {
})

geom_Rlogo <- function(mapping = NULL, data = NULL, stat = "identity", 
                       position = "identity", na.rm = FALSE, show.legend = NA, inherit.aes = TRUE, 
                       ...) {
    layer(data = data, mapping = mapping, stat = stat, geom = GeomRlogo, 
          position = position, show.legend = show.legend, inherit.aes = inherit.aes, 
          params = list(na.rm = na.rm, img = img, ...))
}

# Plot the graph!
p <- ggplot(my_data, aes(x=lyrics_to_lil_wayne, y=Annual_Rainfall_.in..)) + 
    geom_Rlogo() + ylab('Annual rainfall in each US state (z-score)') +
    xlab("\"Lyrics to Lil' Wayne\" Google searches (z-score)") +
    theme(panel.grid.minor = element_blank(),
          panel.grid.major = element_line(linetype = "dotted", colour = "black"),
          axis.title = element_text(face="bold", size=22),
          axis.text=element_text(size=16))

ggsave(filename = "lw.png", plot=p, dpi = 300, width = 10, height = 10)