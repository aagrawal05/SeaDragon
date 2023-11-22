#include <csignal>
#include <iostream>
#include <websocketpp/config/asio_no_tls.hpp>
#include <websocketpp/server.hpp>
#include <chrono>

using Server = websocketpp::server<websocketpp::config::asio>;
using ConnectionHdl = websocketpp::connection_hdl;

void on_message(Server* server, ConnectionHdl hdl,
                websocketpp::config::asio::message_type::ptr msg) {
  std::chrono::system_clock::time_point now = std::chrono::system_clock::now();
  std::chrono::duration<long long, std::milli> duration_since_epoch = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch());
  long long current_time = duration_since_epoch.count();
  std::cout << current_time << " - on_message: " << msg->get_payload() << std::endl;
  server->send(hdl, msg->get_payload(), websocketpp::frame::opcode::text);
}

void turn_off_logging(Server& server) {
  server.clear_access_channels(websocketpp::log::alevel::all);
  server.clear_error_channels(websocketpp::log::elevel::all);
}

void set_message_handler(Server& server) {
  server.set_message_handler(
      websocketpp::lib::bind(&on_message, &server, std::placeholders::_1, std::placeholders::_2));
}

int main() {
  Server server;

  turn_off_logging(server);

  server.init_asio();

  set_message_handler(server);

  server.listen(30001);
  server.start_accept();
  server.run();
}

