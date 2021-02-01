//
// Created by boris on 01.02.2021.
//

#ifndef CHECKERS_CONFIG_H
#define CHECKERS_CONFIG_H

#include <yaml-cpp/yaml.h>
namespace checkers::config {
    struct config_addr {
        std::string host;
        int port;
    };

    struct config {
        config_addr addr;
        std::string db_path;
    };

    config read_config(std::string path) {
        auto rconfig = YAML::LoadFile(path);
        auto host = rconfig["addr"]["host"].as<std::string>();
        auto port = rconfig["addr"]["port"].as<int>();
        auto db_path = rconfig["db"].as<std::string>();
        return config{config_addr{host,port}, db_path};
    }
}

#endif //CHECKERS_CONFIG_H
