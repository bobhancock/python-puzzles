def output_xml(data):
    print("I'm processing XML data!")
    
    

def output(data, format="xml"): 
    output_function = getattr(outprocs,
                              "output_%s" % format,
                              outprocs.output_xml)

    return output_function(data)
