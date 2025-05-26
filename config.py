from src.FileConfig import Config, Files

CONFIG: Config = [
    # Add your file paths here.
    Files(
        client="orico-id", #8
        dashboard="202503/DB/orico-id.csv",
        console="202503/console/orico-id.csv",
        output="202503/merge/orico-id.csv",
    ),
    Files(
        client="mceasy-id", #12
        dashboard="202503/DB/mceasy-id.csv",
        console="202503/console/mceasy-id.csv",
        output="202503/merge/mceasy-id.csv",
    ),
    Files(
        client="cakapcom-id", #12
        dashboard="202503/DB/cakapcom-id.csv",
        console="202503/console/cakapcom-id.csv",
        output="202503/merge/cakapcom-id.csv",
    ),
    Files(
        client="yappika-actionaid-id", #12
        dashboard="202503/DB/yappika-actionaid-id.csv",
        console="202503/console/yappika-actionaid-id.csv",
        output="202503/merge/yappika-actionaid-id.csv",
    ),
    Files(
        client="erablue-id", #12
        dashboard="202503/DB/erablue-id.csv",
        console="202503/console/erablue-id.csv",
        output="202503/merge/erablue-id.csv",
    ),
    #Files(
        #client="efishery-id", #15
        #dashboard="202503/DB/efishery-id.csv",
        #console="202503/console/efishery-id.csv",
        #output="202503/merge/efishery-id.csv",
    #),
    #Files(
        #client="efishery-vc-id", #15
        #dashboard="202503/DB/efishery-vc-id.csv",
        #console="202503/console/efishery-vc-id.csv",
        #output="202503/merge/efishery-vc-id.csv",
    #),

]