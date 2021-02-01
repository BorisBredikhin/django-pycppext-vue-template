#include <iostream>
#include <string>
#include <boost/program_options.hpp>

#include "config.h"

namespace po = boost::program_options;

/**
 *  * @return Описание параметров кпомандной строки
 */
po::options_description get_description();

/**
 *
 * @param argc количество переданных аргументов командной строки
 * @param argv значения переданных аргументов командной строки
 * @param description описание аргументов командной строки
 * @return map значений аргументов командной строки
 */
po::variables_map parse_parameters(int argc, char *const *argv, const po::options_description &description);

int main(int argc, char *argv[]) {
    po::options_description description = get_description();

    po::variables_map variablesMap = parse_parameters(argc, argv, description);

    if (variablesMap.empty() || variablesMap.contains("help"))
        std::cout << description << std::endl;
    if (variablesMap.contains("config")) {
        auto pathToConfig = variablesMap["config"].as<std::string>();
        auto config = checkers::config::read_config(pathToConfig);
        std::cout << "D";
    }
    return 0;
}

po::variables_map parse_parameters(int argc, char *const *argv, const po::options_description &description) {
    po::variables_map variables_map;
    po::store(po::parse_command_line(argc, argv, description), variables_map);
    po::notify(variables_map);
    return variables_map;
}

po::options_description get_description() {
    po::options_description description("Allowed options");

    description.add_options()("help", "produce help message")(
            "config", boost::program_options::value<std::string>(), "path to configuration file"
                                                             );
    return description;
}
