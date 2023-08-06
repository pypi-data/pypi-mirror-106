# EasyGlue

This project aims to make the usage of AWS Glue's DynamicFrame more similar to that of Apache Spark's DataFrame, so that it's easier to remember and read. Let's take a simple S3 read of a JSON dataset for instance:

In Spark, this would be a DataFrame S3 read:
```
spark.read().json('s3://test_path/')
```

In Glue, this would be a DynamicFrame S3 read:
```
glue.create_dynamic_frame.from_options(connection_type='s3', connection_options={'paths': ['s3://test_path/']}, format='json', transformation_ctx='datasource0')
```

As you can see, the syntax here is quite different - and in the case of Glue, way more verbose. With EasyGlue, you can turn the DynamicFrame read operation into something way more similar:
```
glue.read().json('s3://test_path/')
```

## Currently-supported options

The project currently supports:

* Reading/writing from/to:
    * S3, in any of the file formats supported by Glue
    * JDBC
    * RDDs
    * DynamoDB
    * DocumentDB and MongoDB
* Secrets Manager integration for JDBC read/writes

## Usage

You can either use the pre-built PyPi package, or build it yourself to a wheel file:

### Using from PyPi

To use EasyGlue in your projects, simply add the following properties to your job:

```
key: --additional-python-modules
value: easyglue
```

Then add an `import easyglue` statement at the beginning of your job's code. That's it.

### Building to a wheel file

If you prefer to build from source and pass the module as a wheel file, do the following:

1. Download the source code: `git clone https://github.com/albertquiroga/EasyGlue.git`
2. Go into the project's directory, and build it into a wheel file: `python setup.py build bdist_wheel`
3. A new `dist` directory will have been created, inside you'll find the built wheel file. Upload this to S3 and add it as a library to your Glue ETL Job
4. In your ETL Job code, simply add a `import easyglue` line at the top

## How does this work?

This project uses [class extension methods](https://en.wikipedia.org/wiki/Extension_method) to simply add methods to the GlueContext class:

* In Python this is not supported as neatly as in [other programming languages](https://docs.swift.org/swift-book/LanguageGuide/Extensions.html), but it's doable through `setattr`.
* In Scala, this is [directly supported](http://dotty.epfl.ch/docs/reference/contextual/extension-methods.html).

## Roadmap

Check the roadmap in GitHub [here](https://github.com/albertquiroga/EasyGlue/projects/1)
